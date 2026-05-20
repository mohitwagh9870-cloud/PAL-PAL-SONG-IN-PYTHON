import sys
import time
import pygame

def play_full_song():
    pygame.mixer.init()
    try:
        pygame.mixer.music.load("pal_pal.mp3")
    except pygame.error:
        print("Error: 'pal_pal.mp3' not found! Make sure the file is named correctly.")
        return

    lyrics = [
    
        "Pal pal jeena muhaal mera tere bina",
        "Yeh saare nashe bekaar teri aankhon ke siva",
        "Ghar nahi jaata, main bahar, rehta tera intezaar",
        "Mere khwabon mein aa na karke 16 singhaar",
        "",
        "Main ab kyun hosh mein aata nahi?",
        "Sukoon yeh dil kyun paata nahi?",
        "Kyun todun khud se jo the waade?",
        "Ke ab yeh ishq nibhana nahi",
        "",
        "Main modun tumse jo yeh chehra",
        "Dobara nazar milana nahi",
        "Yeh duniya jaane mera dard",
        "Tujhe yeh nazar kyun aata nahi?",
        "",
        "Sohneya, yoon tera sharmana meri jaan na le-le",
        "Kaan ke peechhe zulf chupana, meri jaan, kya kehne!",
        "Zaalima, tauba tera nakhra! Iske waar kya kehne!",
        "Thaam ke baithe dil ko ghayal, kahin haar na baithein",
        "",
        "Teri nazrein mujhse kya kehti hain, inmein wafa behti hai",
        "Thodi-thodi si raazi, thodi si khafa rehti hain",
        "Log hain zaalim bade, inmein jafa dekhi hai",
        "Yeh duniya teri nahi, maine tujh mein haya dekhi hai"
    ]

    # Kept the first part unchanged, but cut down all the following delays to speed it up!
    delays = [
        1.8, 2.8, 2.8,       # Intro Hooks
        1.8, 1.8, 0.8, 0.8,  # Verse 1 Main -> KEPT PERFECT
        0.4,                 # Verse Break (Slightly faster gap)
        1.0, 1.0, 1.0, 1.6,  # Chorus Part 1 -> SPED UP
        0.4,                 # Mid-Chorus Break
        1.8, 1.8, 1.5, 1.4,  # Chorus Part 2 -> SPED UP
        0.6,                 # Bridge Transition to Verse 2
        1.1, 2.7, 2.8, 2.8,  # Verse 2 ("Sohneya...") -> SPED UP
        1.4,                 # Verse Break
        2.8, 2.8, 2.6, 2.8   # Verse 3 ("Teri nazrein...") -> SPED UP
    ]

    print("======== Pal Pal by Mohit ========\n")
    pygame.mixer.music.play()
    
    time.sleep(0.9) 

    for i, line in enumerate(lyrics):
        if line == "":
            print()
            if i < len(delays): 
                time.sleep(delays[i])
            continue
            
        # Character typing speed
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.040) 
            
        print()
        if i < len(delays): 
            time.sleep(delays[i])
        else: 
            time.sleep(0.5)

    while pygame.mixer.music.get_busy(): 
        time.sleep(1)

if __name__ == "__main__":
    play_full_song()
