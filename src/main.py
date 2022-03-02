def generate_letter_lists():
    global a_list,b_list,c_list,d_list,e_list,f_list,g_list,h_list,i_list,j_list,k_list,l_list,m_list
    global n_list,o_list,p_list,q_list,r_list,s_list,t_list,u_list,v_list,w_list,x_list,y_list,z_list
    a_list = []
    b_list = []
    c_list = []
    d_list = []
    e_list = []
    f_list = []
    g_list = []
    h_list = []
    i_list = []
    j_list = []
    k_list = []
    l_list = []
    m_list = []
    n_list = []
    o_list = []
    p_list = []
    q_list = []
    r_list = []
    s_list = []
    t_list = []
    u_list = []
    v_list = []
    w_list = []
    x_list = []
    y_list = []
    z_list = []

# Create a list to store 5 letter words
global five_letter_words_list_all_words
five_letter_words_list_all_words = []

# Open the word database and add 5 letter words to a corresponding list
words_database_file = open("Words_English.txt", 'r')
for line in words_database_file:
    individual_word = line.strip() # Remove the endline character from each line before storing
    if len(individual_word) == 5:
        five_letter_words_list_all_words.append(individual_word) # Add 5 letter word to the list
five_letter_word_list = five_letter_words_list_all_words

# Generate frequency scores for all of the letters
generate_letter_lists()
for word in five_letter_word_list:
    for char in word:
        if char == 'a':
            a_list.append(char)
        if char == 'b':
            b_list.append(char)
        if char == 'c':
            c_list.append(char)
        if char == 'd':
            d_list.append(char)
        if char == 'e':
            e_list.append(char)
        if char == 'f':
            f_list.append(char)
        if char == 'g':
            g_list.append(char)
        if char == 'h':
            h_list.append(char)
        if char == 'i':
            i_list.append(char)
        if char == 'j':
            j_list.append(char)
        if char == 'k':
            k_list.append(char)
        if char == 'l':
            l_list.append(char)
        if char == 'm':
            m_list.append(char)
        if char == 'n':
            n_list.append(char)
        if char == 'o':
            o_list.append(char)
        if char == 'p':
            p_list.append(char)
        if char == 'q':
            q_list.append(char)
        if char == 'r':
            r_list.append(char)
        if char == 's':
            s_list.append(char)
        if char == 't':
            t_list.append(char)
        if char == 'u':
            u_list.append(char)
        if char == 'v':
            v_list.append(char)
        if char == 'w':
            w_list.append(char)
        if char == 'x':
            x_list.append(char)
        if char == 'y':
            y_list.append(char)
        if char == 'z':
            z_list.append(char)
a_score = round(((100*len(a_list))/15918),2)
b_score = round(((100*len(b_list))/15918),2)
c_score = round(((100*len(c_list))/15918),2)
d_score = round(((100*len(d_list))/15918),2)
e_score = round(((100*len(e_list))/15918),2)
f_score = round(((100*len(f_list))/15918),2)
g_score = round(((100*len(g_list))/15918),2)
h_score = round(((100*len(h_list))/15918),2)
i_score = round(((100*len(i_list))/15918),2)
j_score = round(((100*len(j_list))/15918),2)
k_score = round(((100*len(k_list))/15918),2)
l_score = round(((100*len(l_list))/15918),2)
m_score = round(((100*len(m_list))/15918),2)
n_score = round(((100*len(n_list))/15918),2)
o_score = round(((100*len(o_list))/15918),2)
p_score = round(((100*len(p_list))/15918),2)
q_score = round(((100*len(q_list))/15918),2)
r_score = round(((100*len(r_list))/15918),2)
s_score = round(((100*len(s_list))/15918),2)
t_score = round(((100*len(t_list))/15918),2)
u_score = round(((100*len(u_list))/15918),2)
v_score = round(((100*len(v_list))/15918),2)
w_score = round(((100*len(w_list))/15918),2)
x_score = round(((100*len(x_list))/15918),2)
y_score = round(((100*len(y_list))/15918),2)
z_score = round(((100*len(z_list))/15918),2)

# Sort through every word and find the one with the highest net frequency
best_word = ['',0]
optimal_word = []
for word in five_letter_word_list:
    score = 0
    for char in word:
        if char == 'a':
            score += 52.72
        if char == 'b':
            score += 13.12
        if char == 'c':
            score += 17.24
        if char == 'd':
            score += 17.66
        if char == 'e':
            score += 49
        if char == 'f':
            score += 7.78
        if char == 'g':
            score += 12.38
        if char == 'h':
            score += 14.35
        if char == 'i':
            score += 31.83
        if char == 'j':
            score += 2.36
        if char == 'k':
            score += 10.95
        if char == 'l':
            score += 26.67
        if char == 'm':
            score += 15.67
        if char == 'n':
            score += 25.4
        if char == 'o':
            score += 32.79
        if char == 'p':
            score += 14.44
        if char == 'q':
            score += 0.87
        if char == 'r':
            score += 32.31
        if char == 's':
            score += 41.07
        if char == 't':
            score += 26.32
        if char == 'u':
            score += 21.11
        if char == 'v':
            score += 5.52
        if char == 'w':
            score += 7.36
        if char == 'x':
            score += 2.27
        if char == 'y':
            score += 15.84
        if char == 'z':
            score += 2.98
    
    if score > best_word[1]:
        optimal_word.clear()
        for char in word:
            optimal_word.append(char)
            if len(set(optimal_word)) == len(optimal_word): # Check if word has all unique letters
                unique = 1
            else:
                unique = 0
                break
        if unique == 1:
            best_word.clear()
            best_word.append(word)
            best_word.append(score)
    score = 0

print(best_word)