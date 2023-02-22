# ----------------------------- COPY BACKEND ENV ----------------------------- #
FILE1='./api/.env'
if [ ! -f $FILE1 ]; then
    echo "File $FILE1 does not exist, copying 'example.env .'"
    cp ./api/example.env $FILE1
fi

# ------------------------- COPY BLOGGER ENV ------------------------ #
FILE2='./blogger/.env'
if [ ! -f $FILE2 ]; then
    echo "File $FILE2 does not exist, copying 'example.env .'"
    cp ./blogger/example.env $FILE2
fi

docker compose up -d --build