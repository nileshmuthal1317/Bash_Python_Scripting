=== File: conditional.sh ===
#!/bin/bash

num_a=100
num_b=200

if [ $num_a -lt $num_b ]; then
        echo "$num_a is less than $num_b!"
else
        echo "$num_a is greater than $num_b"
fi

=== End of conditional.sh ===

=== File: for.sh ===
#!/bin/bash

5yrh=ee1;


nfahul
ravi
saurabh
lahavit
bash
scripting

=== End of for.sh ===

=== File: function.sh ===
#!/bin/bash

# This is the practice for function which used for reuse purpose

function user_details {
        echo "User Name: $(whoami)"
        echo "Home Dir: $HOME"
}

user_details # calling the function by just it's name
user_details # recalling the function

=== End of function.sh ===

=== File: numsrtingcomparison.sh ===
#!/bin/bash

string_a="UNIX"
string_b="GNU"

echo "Are $string_a and $string_b strings equal?"
[ $string_a = $string_b ]
echo $?

num_a=100
num_b=100

echo "Are $num_a and $num_b equal?"
[ $num_a = $num_b ]
echo $?

=== End of numsrtingcomparison.sh ===

=== File: until.sh ===
#!/bin/bash

counter=6
until [ $counter -lt 3 ]; do
        let counter-=1
        echo $counter
done

=== End of until.sh ===

=== File: welcome.sh ===
#!/bin/bash

greeting="Welcome" # declating string datatype variable
user=$(whoami) # storing bash command output in variable
day=$(date +%A)

echo "$greeting back $user! Today is $day" # printing the line and calling variable inside
echo "Bash shell version: $BASH_VERSION. Enjoy!"

=== End of welcome.sh ===

=== File: while.sh ===
#!/bin/bash

counter=0
while [ $counter -lt 3 ]; do
        let counter+=1
        echo $counter
done

=== End of while.sh ===
