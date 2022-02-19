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

a_frequency = round(((100*len(a_list))/15918),2)
b_frequency = round(((100*len(b_list))/15918),2)
c_frequency = round(((100*len(c_list))/15918),2)
d_frequency = round(((100*len(d_list))/15918),2)
e_frequency = round(((100*len(e_list))/15918),2)
f_frequency = round(((100*len(f_list))/15918),2)
g_frequency = round(((100*len(g_list))/15918),2)
h_frequency = round(((100*len(h_list))/15918),2)
i_frequency = round(((100*len(i_list))/15918),2)
j_frequency = round(((100*len(j_list))/15918),2)
k_frequency = round(((100*len(k_list))/15918),2)
l_frequency = round(((100*len(l_list))/15918),2)
m_frequency = round(((100*len(m_list))/15918),2)
n_frequency = round(((100*len(n_list))/15918),2)
o_frequency = round(((100*len(o_list))/15918),2)
p_frequency = round(((100*len(p_list))/15918),2)
q_frequency = round(((100*len(q_list))/15918),2)
r_frequency = round(((100*len(r_list))/15918),2)
s_frequency = round(((100*len(s_list))/15918),2)
t_frequency = round(((100*len(t_list))/15918),2)
u_frequency = round(((100*len(u_list))/15918),2)
v_frequency = round(((100*len(v_list))/15918),2)
w_frequency = round(((100*len(w_list))/15918),2)
x_frequency = round(((100*len(x_list))/15918),2)
y_frequency = round(((100*len(y_list))/15918),2)
z_frequency = round(((100*len(z_list))/15918),2)



print("A Frequency:", round(((100*len(a_list))/15918),2))
print("B Frequency:", round(((100*len(b_list))/15918),2))
print("C Frequency:", round(((100*len(c_list))/15918),2))  
print("D Frequency:", round(((100*len(d_list))/15918),2))
print("E Frequency:", round(((100*len(e_list))/15918),2))
print("F Frequency:", round(((100*len(f_list))/15918),2))
print("G Frequency:", round(((100*len(g_list))/15918),2))
print("H Frequency:", round(((100*len(h_list))/15918),2))
print("I Frequency:", round(((100*len(i_list))/15918),2))
print("J Frequency:", round(((100*len(j_list))/15918),2))
print("K Frequency:", round(((100*len(k_list))/15918),2))
print("L Frequency:", round(((100*len(l_list))/15918),2))
print("M Frequency:", round(((100*len(m_list))/15918),2))
print("N Frequency:", round(((100*len(n_list))/15918),2))
print("O Frequency:", round(((100*len(o_list))/15918),2))
print("P Frequency:", round(((100*len(p_list))/15918),2))
print("Q Frequency:", round(((100*len(q_list))/15918),2))
print("R Frequency:", round(((100*len(r_list))/15918),2))
print("S Frequency:", round(((100*len(s_list))/15918),2))
print("T Frequency:", round(((100*len(t_list))/15918),2))
print("U Frequency:", round(((100*len(u_list))/15918),2))
print("V Frequency:", round(((100*len(v_list))/15918),2))
print("W Frequency:", round(((100*len(w_list))/15918),2))
print("X Frequency:", round(((100*len(x_list))/15918),2))
print("Y Frequency:", round(((100*len(y_list))/15918),2))
print("Z Frequency:", round(((100*len(z_list))/15918),2))

        
        
        



print(len(five_letter_word_list))