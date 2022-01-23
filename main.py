string_array = ["found", "array", "sting", "young", "proxy"]

# intake array of strings, record frequency of letters
def record_frequency(intake_string_array):
    a_freq = 0
    b_freq = 0
    c_freq = 0
    d_freq = 0
    e_freq = 0
    f_freq = 0
    g_freq = 0
    h_freq = 0
    i_freq = 0
    j_freq = 0
    k_freq = 0
    l_freq = 0
    m_freq = 0
    n_freq = 0
    o_freq = 0
    p_freq = 0
    q_freq = 0
    r_freq = 0
    s_freq = 0
    t_freq = 0
    u_freq = 0
    v_freq = 0
    w_freq = 0
    x_freq = 0
    y_freq = 0
    z_freq = 0
    for word in intake_string_array:
        for letter in word:
            if (letter == 'a'):
                a_freq += 1
            elif (letter == 'b'):
                b_freq += 1
            elif (letter == 'c'):
                c_freq += 1
            elif (letter == 'd'):
                d_freq += 1
            elif (letter == 'e'):
                e_freq += 1
            elif (letter == 'f'):
                f_freq += 1
            elif (letter == 'g'):
                g_freq += 1
            elif (letter == 'h'):
                h_freq += 1
            elif (letter == 'i'):
                i_freq += 1
            elif (letter == 'j'):
                j_freq += 1
            elif (letter == 'k'):
                k_freq += 1
            elif (letter == 'l'):
                l_freq += 1
            elif (letter == 'm'):
                m_freq += 1
            elif (letter == 'n'):
                n_freq += 1
            elif (letter == 'o'):
                o_freq += 1
            elif (letter == 'p'):
                p_freq += 1
            elif (letter == 'q'):
                q_freq += 1
            elif (letter == 'r'):
                r_freq += 1
            elif (letter == 's'):
                s_freq += 1
            elif (letter == 't'):
                t_freq += 1
            elif (letter == 'u'):
                u_freq += 1
            elif (letter == 'v'):
                v_freq += 1
            elif (letter == 'w'):
                w_freq += 1
            elif (letter == 'x'):
                x_freq += 1
            elif (letter == 'y'):
                y_freq += 1
            elif (letter == 'z'):
                z_freq += 1
            else:
                pass  # TODO: Log string items marked as non-letters
    print("The letter A appeared " + str(a_freq) + " times")
    print("The letter B appeared " + str(b_freq) + " times")
    print("The letter C appeared " + str(c_freq) + " times")
    print("The letter D appeared " + str(d_freq) + " times")
    print("The letter E appeared " + str(e_freq) + " times")
    print("The letter F appeared " + str(f_freq) + " times")
    print("The letter G appeared " + str(g_freq) + " times")
    print("The letter H appeared " + str(h_freq) + " times")
    print("The letter I appeared " + str(i_freq) + " times")
    print("The letter J appeared " + str(j_freq) + " times")
    print("The letter K appeared " + str(k_freq) + " times")
    print("The letter L appeared " + str(l_freq) + " times")
    print("The letter M appeared " + str(m_freq) + " times")
    print("The letter N appeared " + str(n_freq) + " times")
    print("The letter O appeared " + str(o_freq) + " times")
    print("The letter P appeared " + str(p_freq) + " times")
    print("The letter Q appeared " + str(q_freq) + " times")
    print("The letter R appeared " + str(r_freq) + " times")
    print("The letter S appeared " + str(s_freq) + " times")
    print("The letter T appeared " + str(t_freq) + " times")
    print("The letter U appeared " + str(u_freq) + " times")
    print("The letter V appeared " + str(v_freq) + " times")
    print("The letter W appeared " + str(w_freq) + " times")
    print("The letter X appeared " + str(x_freq) + " times")
    print("The letter Y appeared " + str(y_freq) + " times")
    print("The letter Z appeared " + str(z_freq) + " times")

record_frequency(string_array)
input(" ")
