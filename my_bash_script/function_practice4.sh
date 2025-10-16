# Define the function
function memory_check() {
server_name=$(hostname)
echo ""
echo "The current memory usage on ${server_name} is: "
free -h
echo ""
}
# Call the function
memory_check
