#! /bin/bash

#obtener archivo para guardar contenido de /etc/passwd

outputFile=$1

cat /etc/passwd > $outputFile  #Req1. Contenido de etc/passwd al archivo dado por user

echo "----------------------------------------------------------------" >> $outputFile


filesfound=$(sudo find /var -name messages) # buscamos cada archivo messages dentro de /var

if [ ${#filesfound} -gt 0 ] #revisar si el comando find encontró algo
then
    sudo stat $filesfound >> $outputFile
fi #se describe cada archivo usando su direccion encontrada y se agrega al file

filesfound=$(sudo find /var -name secure) # buscamos cada archivo secure dentro de /var

if [ ${#filesfound} -gt 0 ]
then
    sudo stat $filesfound >> $outputFile
fi

filesfound=$(sudo find /var -name auth.log) # buscamos cada archivo secure dentro de /var

if [ ${#filesfound} -gt 0 ]
then
    sudo stat $filesfound >> $outputFile
fi

echo "----------------------------------------------------------------" >> $outputFile

while read line 
do
    if [[ $line == bin* ]] #si la linea comienza con bin, entonces guarda la linea en el outputfile
    then
        echo "$line" >> $outputFile
    fi
done < "/etc/passwd" #toma el valor del file y revisa linea por linea.

echo "Done! See the file created with the name you specified: "
echo "$outputFile"

#cat outputFile

