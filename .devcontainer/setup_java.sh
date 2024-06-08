# setup_java.sh
#!/bin/bash

# setup_java.sh
#!/bin/bash

source "$HOME/.sdkman/bin/sdkman-init.sh"
yes | sdk install java 8.0.292-zulu
sdk default java 8.0.292-zulu
java -version