# Read from the file file.txt and print its transposed content to stdout.
column=$(awk '{print NF}' file.txt | uniq)
for((i=1;i<=column;i++))
do
  cut -d' ' -f$i file.txt|xargs
done
