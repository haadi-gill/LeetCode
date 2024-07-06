
# 193. Valid Phone Numbers

# Given a text file file.txt that contains a list of phone numbers (one per line), write a one-liner bash script to print all valid phone numbers.

# You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

# You may also assume each line in the text file must not contain leading or trailing white spaces.

# Example:

# Assume that file.txt has the following content:

# 987-123-4567
# 123 456 7890
# (123) 456-7890

# Your script should output the following valid phone numbers:

# 987-123-4567
# (123) 456-7890



# Read from the file file.txt and output all valid phone numbers to stdout.

while read -r CURRENT_LINE; do
    
    # if [ "${CURRENT_LINE:0:1}" == "(" ]; then
    #     if [ "${CURRENT_LINE:4:2}" == ") " ]; then
    #         if [ "${CURRENT_LINE:9:1}" == "-" ]; then
    #             if [ $(expr length "$CURRENT_LINE") == 14 ]; then
    #                 echo "$CURRENT_LINE"
    #             fi
    #         fi
    #     fi
    # else
    #     if [ "${CURRENT_LINE:3:1}" == "-" ]; then
    #         if [ "${CURRENT_LINE:7:1}" == "-" ]; then
    #             if [ $(expr length "$CURRENT_LINE") == 12 ]; then
    #                 echo "$CURRENT_LINE"
    #             fi
    #         fi
    #     fi
    # fi
    
    
    if [[ "$CURRENT_LINE" =~ ^(\([0-9]{3}\)[[:space:]]|[0-9]{3}-)[0-9]{3}-[0-9]{4}$ ]]; then
        echo "$CURRENT_LINE"
    fi
    
done < "file.txt"