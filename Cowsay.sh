sudo apt-get install cowsay -y

/usr/games/cowsay -f dragon "Run for cover, I am a Dragon....RAWR" >> dragon.txt

grep -i "dragon" dragon.txt
cat dragon.txt
ls