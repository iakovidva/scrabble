# Perigrafei antikeimena pou leitoyrgoun ws sakoulaki me ta grammata tou paixnidou
import random
import itertools
import json
import sys


words = [line.strip() for line in open("greek7.txt", 'r')]

class SakClass:
    '''
    Η κλάση SakClass υλοποιεί το ρόλο που έχει το σακουλάκι στο παιχνίδι του scrabble. Έχει μέσα τα γράμματα του αλφαβήτου,
    τις φορές που εμφανίζονται και τους πόντους που πιάνουν στο λεξικό lets. Η letlist είναι αυτή που έχει τον ρόλο του σακουλιού,
    έχοντας μέσα τα γράμματα αυτά ανακατεμένα. Στον κατασκευαστή φτιάχνεται το σακουλάκι, με την κλήση της μεθόδου randomize_sak.
    Σε αυτή αρχικά γίνονται append όλα τα γράμματα μέσα στη λίστα letlist, έπειτα ανακατεύονται και επιστρέφεται η τελική τους
    μορφή.. Η συνάρτηση getLetters επιστρέφει όσα γράμματα ζητηθούν με την βοήθεια μιας λίστας letters_to_get. Τέλος, η putBackLetters
    δέχεται μια λίστα γραμμάτων την οποία και ξανά προσθέτει στο σακουλάκι, δηλαδή στη λίστα letlist.
    '''
    lets = {'Α':[12,1],'Β':[1,8],'Γ':[2,4],'Δ':[2,4],'Ε':[8,1],
                    'Ζ':[1,10],'Η':[7,1],'Θ':[1,10],'Ι':[8,1],'Κ':[4,2],
                    'Λ':[3,3],'Μ':[3,3],'Ν':[6,1],'Ξ':[1,10],'Ο':[9,1],
                    'Π':[4,2],'Ρ':[5,2],'Σ':[7,1],'Τ':[8,1],'Υ':[4,2],
                    'Φ':[1,8],'Χ':[1,8],'Ψ':[1,10],'Ω':[3,3]}

    letlist = []

    def __init__(self):
        self.randomize_sak()

    # Γίνεται εισαγωγή των γραμμάτων στην letlist σύμφωνα με το dict lets. Στην συνέχεια τα γράμματα ανακατεύονται. 
    def randomize_sak(self):
        for l in SakClass.lets:
            for _t in range(SakClass.lets[l][0]):
                SakClass.letlist.append(l)
        megethos = len(SakClass.letlist)
        shuffle = random.sample(range(0,megethos),megethos)
        random_let_list = []
        for i in range (0,megethos):
            random_let_list.append(SakClass.letlist[shuffle[i]])
        SakClass.letlist = random_let_list
        return SakClass.letlist

    # Ανακάτεμα των γραμμάτων και pop όσων χρειαστεί ανάλογα με την κάθε περίπτωση. Επιστρέφει λίστα με γράμματα.
    @staticmethod
    def getLetters(N):
        random.shuffle(SakClass.letlist)
        letters_to_get = []
        for _ in range(N):
            letters_to_get.append(SakClass.letlist.pop())

        return letters_to_get

    # Δέχεται γράμματα και τα βάζει πίσω στην letlist
    @staticmethod
    def putBackLetters(letters):
        SakClass.letlist.extend(letters)

# Βασική κλάση από την οποία παράγονται η Human και η Computer. Έχει 2 ιδιότητες, letter_list η οποία και επεκτείνεται με την
# κατασκευή του αντικειμένου με 7 γράμματα από το σακουλάκι και την score. 
class Player:

    def __init__(self):
        self.letters_list = []
        self.score = 0
        self.letters_list.extend(SakClass.getLetters(7))

    def __repr__(self):
        return 'The list of player\'s letters: {}\nPlayer\'s score: {}'.format(self.letters_list,self.score)

# Κλάση παράγωγη της Player, υπεύθυνη για το παιχνίδι του παίκτη.
class Human(Player):
    '''
        Με την δημιουργία του ο παίκτης παίρνει 7 γράμματα από το σακουλάκι και ένα αρχικό σκορ = 0, 
        κληρονομώντας αυτές τις δύο ιδιότητες από την Player. Του εμφανίζονται τα γράμματα του και του
        ζητείται να δώσει λέξη με αυτά. Αν η λέξη που δίνει ανήκει στο λεξικό, ελέγχω κάθε γράμμα
        να υπάρχει στα γράμματα του παίκτη. Αν κάποιο δεν υπάρχει εμφανίζει κατάλληλο μήνυμα και
        σταματάει. Αν υπάρχουν όλα, εμφανίζεται μήνυμα, σβήνουμε από τον παίκτη τα γράμματα που
        έδωσε για την λέξη, συμπληρώνουμε από το σακουλάκι για να έχει 7 και αυξάνουμε το σκορ του.
        Αν επιλέξει 'p' επιστρέφονται στο σακουλάκι τα γράμματα του παίκτη, αδειάζει η λίστα με τα
        γράμματα του και ξανά γεμίζεται με άλλα 7 γράμματα. Διαφορετικά έχει δώσει κάτι άκυρο.
    '''

    def __init__(self):
        Player.__init__(self)

    def __repr__(self):
        Player.__repr__(self)

    def play(self):
        playerFlag = True
        print('\nΣτο σακουλάκι υπάρχουν {} γράμματα. Σειρά σου!'.format(len(SakClass.letlist)))
        finish = False
        while not finish:
            print('\t\tΔιαθέσιμα γράμματα:')
            for l in self.letters_list:
                print(l,':', SakClass.lets[l][1],end='\t')
            print()
            word = input('Δώσε λέξη:\t')
            word_points = 0
            valid_word = True
        
            if word in words:
                temp_letters = self.letters_list[:]
                for letter in word:
                    if letter not in temp_letters:
                        print('Δεν έχεις όλα τα γράμματα της λέξης!')
                        word_points = 0
                        valid_word = False
                        break
                    temp_letters.remove(letter)
                    word_points = word_points + SakClass.lets[letter][1]
                if valid_word: 
                    print('---> Η λέξη {} σου έδωσε {} πόντους'.format(word, word_points))
                    if ( (7-len(temp_letters)) > len(SakClass.letlist) ):
                        print('Τα γράμματα στο σακουλάκι δεν φτάνουν για τον χρήστη')
                        print('Τέλος παιχνιδιού')
                        playerFlag = False
                    else:
                        self.letters_list = temp_letters[:]
                        self.letters_list.extend(SakClass.getLetters(7-len(self.letters_list)))
                    finish = True
                self.score += word_points
                input('Πάτα κάτι για να παίξει το bot. ')
            elif (word == 'p'):
                print('Τα γράμματα σου άλλαξαν!, Περίμενε τον επόμενο γύρο.')
                SakClass.putBackLetters(self.letters_list)
                self.letters_list.clear()
                self.letters_list = SakClass.getLetters(7)
                finish = True
            elif (word == 'q'):
                print('Έξοδος παιχνιδιού')
                finish = True
                playerFlag = False
            else:
                print('\nΗ λέξη που έδωσες δεν είναι δεκτή! Προσπάθησε πάλι ή δώσε "p" για πάσο.')

        return playerFlag
        

    def printing(self):
        print('human letters: ', self.letters_list)

# Κλάση παράγωγη της Player, υπεύθυνη για το παιχνίδι του bot.
class Computer(Player):
    '''
    Με την δημιουργία του παίκτη bot, παίρνει 7 γράμματα τα οποία και αφαιρούνται από το σακίδιο καθώς και
    αρχικοποιείται το σκορ στο 0, με την κλήση του κατασκευαστή της ανώτερης κλάσης Person.
    Υπάρχει ένα λεξικό που κρατάει τις λέξεις που έχει βρει το bot καθώς και ένα με αυτές τις λέξεις
    ταξινομημένες σύφωνα με το σκορ. Εμφανίζονται τα γράμματα του παίκτη. Παράγονται όλοι οι συνδιασμοί
    από 1 μέχρι 7 γράμματα και αποθηκεύονται οι αποδεκτές λέξεις μαζί με το σκορ τους. Ταξινομούνται και
    επιλέγεται να παιχτεί μία από τις πρώτες 4 επιλογές του bot, καθώς υλοποιείται ο αλγόριθμος SMART-FAIL.
    Συμπληρώνονται τα γράμματα του.

    '''

    def __init__(self):
        Player.__init__(self)

    def __repr__(self):
        Player.__repr__(self)

    def play(self):
        botFlag = True
        found_words = {}
        sorted_words = {}

        print('\nΣτο σακουλάκι υπάρχουν {} γράμματα. Παίζει το bot!'.format(len(SakClass.letlist)))
        print('\t\tΤα γράμματα του bot:')
        for l in self.letters_list:
            print(l,':', SakClass.lets[l][1],end='\t')
        print()

        for size in range(1,8):
            perms = list(itertools.permutations(self.letters_list,r=size))
            for p in perms:
                lexi = ''.join([str(gramma) for gramma in p])   #Λέξη από permutation
                score = 0
                if (lexi in words and lexi not in found_words):
                    for letter in lexi:
                        score = score + SakClass.lets[letter][1]
                    found_words[lexi] = score

        if len(found_words) > 0: #Έλεγχος ότι έχει βρει λέξη το bot.
            sorted_words = sorted(found_words.items(), key=lambda kv: kv[1], reverse=True) #Ταξινόμηση λέξεων με βάση το σκορ.
            if len(found_words)>=4 : pick = random.randint(0,3)
            else: pick = 0
            word = sorted_words[pick]
            print('Ο αντίπαλος διάλεξε την {} καλύτερη επιλογή του\n---> Η λέξη:{} έδωσε στο bot {} πόντους'.format(pick+1, word[0],word[1]))
            #Αφαιρούνται τα γράμματα που έπαιξε
            for l in word[0]:
                self.letters_list.remove(l)
            #Συμπληρώνονται τα γράμματα 
            if ( (7-len(self.letters_list)) > len(SakClass.letlist) ):
                        print('Τα γράμματα στο σακουλάκι δεν φτάνουν για το bot')
                        print('Τέλος παιχνιδιού')
                        botFlag = False
            else:
                self.letters_list.extend(SakClass.getLetters(7-len(self.letters_list)))
            self.score += word[1] #Αυξάνεται το σκορ του μποτ
        else:   #Αν δεν βρει λέξη, επιστρέφει False ώστε να τερματίσει το παιχνίδι.
            print('Το bot δεν βρήκε κάποια λέξη!')
            botFlag = False
            
        return botFlag

#perigrafei to pws ekselissetai mia partida-game
class Game:
    '''
    Η κλάση Game είναι υπεύθυνη για όλη την εξέλιξη του παιχνιδιού. Με την κατασκευή ενός αντικειμένου Game δημιουργούνται ένα σακίδιο, ένας παίκτης
    και ένα bot. Με την μέθοδο setup() υλοποιούνται όλες οι ενέργειες που απαιτούνται κατά την εκίννηση του παιχνιδιού. Ανοίγει το αρχείο της βάσης
    που περιέχει τα δεδομένα που αποθηκεύονται από τα παιχνίδια, αν δεν μπορεί να το ανοίξει, δημιουργεί ένα καινούριο παίρνωντας την κατάλληλη μορφή
    με τη βοήθεια της createDB(). Έπειτα τυπώνεται το μενού επιλογών, γίνεται έλεγχος ορθότητας, και ανάλογα με το τι έχει επιλέξει ο χρήστης καλείται
    η κατάλληλη μέθοδος. Η μέθοδος run() αναλαμβάνει το τρέξιμο του παιχνιδιού. Τρέχει όσο καμία συνθήκη τερματισμού του παιχνιδιού δεν έχει παραβιαστεί.
    Αυτό γίνεται με την επιστροφή True, False από τις κλήσεις self.player.play(), self.bot.play(). Όταν τελειώσει το παιχνίδι καλείται η end() για να
    εκτελέσει όλες τις ενέργεις που απαιτούνται κατά το κλείσιμο του παιχνιδιού, στέλνοντας μαζί και τους γύρους που κράτησε το παιχνίδι. Η end() αρχικά
    ελέγχει για το ποιος ήταν ο νικητής του παιχνιδιού εμφανίζοντας κατάλληλο μήνυμα και έπειτα καλεί την updateStats(). Η updateStats() ενημερώνει όλες
    τις μεταβλητές που είναι να αλλάξουν μετά το πέρας του παιχνιδιού, ανοίγει το αρχείο βάσης και γράφει τα νέα αποτελέσματα. Αν ο χρήστης επιλέξει
    να δει τα στατιστικά που έχει στο παιχνίδι καλείται η printStats η οποία απλά τυπώνει στην οθόνη με κατάλληλα μηνύματα τις εγγραφές του αρχείου. 
    Η μέθοδος Settings δίνει την δυνατότητα να μηδενιστεί το αρχείο με τα σκορ. 
    '''


    def __init__(self):
        self.sak = SakClass()
        self.player = Human()
        self.bot = Computer()

    def __repr__(self):
        return 'Στη setup γίνεται η εκκίνηση του προγράμματος.  Από εκεί και πέρα ανάλογα με την επιλογή του χρήστη καλείται η κατάλληλη συνάρτηση. \
            Η Game() προσφέρει 3 ιδιότητες σε κάθε αντικείμενο της, ενα σακίδιο, έναν παίκτη και ένα μποτ. '

    # Φόρτωση του αρχείου βάσης, εμφάνιση του μενού, κλήση κατάλληλης συνάρτησης ανάλογα με την επιλογή του χρήστη.
    def setup(self):
        print()
        try:
            with open('db.json','r') as read_file:
                self.data = json.load(read_file)
        except:
            print('Δημιουργία νέας βάσης δεδομένων')
            with open('db.json','w') as write_file:
                json.dump(self.createDB(),write_file)
                self.data = self.createDB()
            
        self.printMenu()
        choise = input('Επιλογή: \t')
        while (choise != '1' and choise != '2' and choise !='3'and choise != 'q'):
            print('Λάθος Επιλογή!\n')
            self.printMenu()
            choise = input('Επιλογή: \t')    
        if choise == '1':
            self.printStats()
            input('\nΠάτα κάτι για να γυρίσεις στο μενού   ')
            self.setup()
        elif choise == '2':
            self.Settings()
            input('\nΠάτα κάτι για να γυρίσεις στο μενού   ')
            self.setup()
        elif choise == '3':
            self.run()
        elif choise == 'q':
            print('Έξοδος παιχνιδιού')
            sys.exit()

    def run(self):
        rounds = 1
        while True:
            print('\n\n\n',20*'~','Γύρος: ',rounds,20*'~')
            if(not(self.player.play())) : break
            if(not(self.bot.play())) : break
            print('Σκορ μετά τον γύρο: {}: {} - {}'.format(rounds,self.player.score,self.bot.score))
            rounds += 1
        self.end(rounds-1)

    def end(self,rounds):
        if (self.player.score > self.bot.score):
            print('Σκορ παίκτη: ', self.player.score, ', Σκορ bot: ', self.bot.score)
            print('Νίκη!')
        elif (self.player.score == self.bot.score):
            print('Σκορ παίκτη: ', self.player.score, ', Σκορ bot: ', self.bot.score)
            print('Ισοπαλία!')
        else:
            print('Σκορ παίκτη: ', self.player.score, ', Σκορ bot: ', self.bot.score)
            print('Ήττα!')
        self.updateStats(rounds)


    #Εμφάνιση του μενού εκκίνησης του προγράμματος.
    def printMenu(self):
        print(5*'*','SCRABBLE',5*'*')
        print(20*'-')
        print('1: Σκορ\n2: Ρυθμίσεις\n3: Παιχνίδι\nq: Έξοδος\n',20 * '-')
    
    #Εμφάνιση των δεδομένων της βάσης.
    def printStats(self):
        print(f'Ο παίκτης έχει %d νίκες' % self.data['Player Wins'])
        print(f'Ο παίκτης έχει %d ήττες' % self.data['Bot Wins'])
        print(f'Ο παίκτης έχει %d ισσοπαλίες' % self.data['Draws'])
        print('Γύροι που έχουν παιχτεί: ', self.data['Total Rounds Played'])
        print('Παιχνίδια που έχουν παιχτεί: ', self.data['Total Games Played'])
        print('Συνολικοί πόντοι παίκτη: ', self.data['Sum Player\'s Points'])
        print('Συνολικοί πόντοι bot: ', self.data['Sum Bot\'s Points'])
        
    #Η μόνη επιλογή στις ρυθμίσεις είναι ο μηδενισμός του αρχείου δεδομένων. Σε περίπτωση που ο χρήστης επιλέξει αυτή τη λειτουργία δίνοντας 1, δημιουργείται
    #νέα βάση και εγγράφεται στο αρχείο db.json. Υπάρχει σκέψη για περισσότερες ρυθμίσεις για αυτό και η print και η επιλογή του χρήστη.
    def Settings(self):
        print('1: Reset Scores')
        choise = input('Επιλογή: ')
        if choise == '1':
            newdata={}
            for d in self.data:
                newdata[d] = 0
            try:
                with open('db.json','w') as write_file:
                    json.dump(newdata, write_file)
            except:
                print('Σφάλμα κατά την ενημέρωση βάσης δεδομένων')
                sys.exit()

    #Ελέγχεται ο νικητής. Ενημερώνονται το λεξικό data που έχει τα δεδομένα της βάσης και τα ξανά γράφει στο αρχείο db.json. Αν αυτό για κάποιο λόγο
    #δεν είναι δυνατό, εμφανίζεται κατάλληλο μήνυμα και τερματίζει το πρόγραμμα.
    def updateStats(self,rounds):

        if (self.player.score > self.bot.score):
            self.data['Player Wins'] += 1
        elif (self.player.score == self.bot.score):
            self.data['Draws'] += 1
        else:
            self.data['Bot Wins'] += 1
        
        self.data['Sum Player\'s Points'] += self.player.score
        self.data['Sum Bot\'s Points'] += self.bot.score
        self.data['Total Games Played'] += 1
        self.data['Total Rounds Played'] += rounds

        try:
            with open('db.json','w') as write_file:
                json.dump(self.data, write_file)
        except:
            print('Σφάλμα κατά την ενημέρωση βάσης δεδομένων')
            sys.exit()
    
    #Δημιουργία λεξικού με τα στατιστικά που κρατάει η βάση και επιστροφή αυτού.
    def createDB(self):
        db = {
            'Player Wins' : 0,
            'Draws' : 0,
            'Bot Wins' : 0,
            'Sum Player\'s Points': 0,
            'Sum Bot\'s Points': 0,
            'Total Games Played': 0,
            'Total Rounds Played':0
        }
        return db