CPPC = g++
CC = gcc


EXECOUTDIR = out
ODIR = server/build

CFLAGSSERV = -lpthread -lcrypto -ldl -fpermissive
CINCSERV = server/includes
SSRCPATH = server/src
CFILESSERV =  $(SSRCPATH)/common.cpp $(SSRCPATH)/main.cpp $(SSRCPATH)/module.cpp $(SSRCPATH)/netinst.cpp $(SSRCPATH)/server.cpp 
#$(SSRCPATH)/api.cpp
CFLAGSCLI = -lssh -lcurl
CFILESCLI = agent/client.c agent/agent.c agent/b64.c agent/beacon.c agent/shell.c

CFLAGSREL = -s
CFLAGSDBG = -ggdb -Wall

CFLAGSSO = -c -fpic -static -lssh -lcrypto
CFILESSO = server/ssh_transport/ssh_transport.cpp server/b64.cpp server/authenticate.cpp server/misc.cpp server/agents.cpp

OBJECT_FILES = $(CFILESSO:%.cpp=$(ODIR)/%.o)

release: #$(OBJECT_FILES)
ifeq (,$(wildcard out))
	@mkdir -p out/shared
endif
	$(CPPC) -o $(EXECOUTDIR)/server.out $(CFILESSERV) $(CFLAGSSERV) -I$(CINCSERV) $(CFLAGSREL)
	$(CC) -o $(EXECOUTDIR)/agent.out $(CFILESCLI) $(CFLAGSCLI) $(CFLAGSREL)

	$(CPPC) -shared -o $(EXECOUTDIR)/shared/ssh_transport.so $(OBJECT_FILES) -lcrypto -lssh
	/bin/bash ./python/update_uis.sh

server_release: #$(OBJECT_FILES)
ifeq (,$(wildcard out))
	@mkdir -p out/shared
endif
	$(CPPC) -o $(EXECOUTDIR)/server.out $(CFILESSERV) $(CFLAGSSERV) -I$(CINCSERV) $(CFLAGSREL)
	#$(CPPC) -shared -o $(EXECOUTDIR)/shared/ssh_transport.so $(OBJECT_FILES) -lcrypto -lssh

server_debug: #$(OBJECT_FILES)
ifeq (,$(wildcard out))
	@mkdir -p out/shared
endif
	$(CPPC) -o $(EXECOUTDIR)/server.out $(CFILESSERV) $(CFLAGSSERV) -I$(CINCSERV) $(CFLAGSDBG)
	#$(CPPC) -shared -o $(EXECOUTDIR)/shared/ssh_transport.so $(OBJECT_FILES) -lcrypto -lssh


debug:# $(OBJECT_FILES)
ifeq (,$(wildcard out))
	@mkdir -p out/shared
endif
	$(CPPC) -o $(EXECOUTDIR)/server.out $(CFILESSERV) $(CFLAGSSERV) -I$(CINCSERV) $(CFLAGSDBG)
	$(CC) -o $(EXECOUTDIR)/agent.out $(CFILESCLI) $(CFLAGSCLI) $(CFLAGSDBG)
	$(CPPC) -shared -o $(EXECOUTDIR)/shared/ssh_transport.so $(OBJECT_FILES) -lcrypto -lssh
	@/bin/bash ./python/update_uis.sh

clean:
	rm -r $(ODIR)

.PHONY: debug release clean server_debug server_release

$(OBJECT_FILES): $(ODIR)/%.o: %.cpp
	@echo "Compiling $<"
	#@mkdir -p $(@D)
	#@$(CPPC) $(CFLAGSSO) -o $@ $<
