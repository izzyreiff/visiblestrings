# dictionary.py
titles = {}
for i in range(1, 31): # Adjust for number of songs in album
    title = f"4_{i}.txt" # Adjust for album #
    titles[f"Title{i}"] = title
import json
titles_json = json.dumps(titles, indent=4)
print(titles_json)

dict = {
    "Tim McGraw": "1_1.txt",
    "Picture To Burn": "1_2.txt",
    "Teardrops on My Guitar": "1_3.txt",
    "A Place In This World": "1_4.txt",
    "Cold As You": "1_5.txt",
    "The Outside": "1_6.txt",
    "Tied Together with a Smile": "1_7.txt",
    "Stay Beautiful": "1_8.txt",
    "Should've Said No": "1_9.txt",
    "Mary's Song (Oh My My My)": "1_10.txt",
    "Our Song": "1_11.txt",
    "I'm Only Me When I'm With You": "1_12.txt",
    "Invisible": "1_13.txt",
    "A Perfectly Good Heart": "1_14.txt",
    "Fearless": "2_1.txt",
    "Fifteen": "2_2.txt",
    "Love Story": "2_3.txt",
    "Hey Stephen": "2_4.txt",
    "White Horse": "2_5.txt",
    "You Belong With Me": "2_6.txt",
    "Breathe (feat. Colbie Caillat)": "2_7.txt",
    "Tell Me Why": "2_8.txt",
    "You're Not Sorry": "2_9.txt",
    "The Way I Loved You": "2_10.txt",
    "Forever & Always": "2_11.txt",
    "The Best Day": "2_12.txt",
    "Change": "2_13.txt",
    "Jump Then Fall": "2_14.txt",
    "Untouchable": "2_15.txt",
    "Come In With The Rain": "2_16.txt",
    "Superstar": "2_17.txt",
    "The Other Side Of The Door": "2_18.txt",
    "Today Was A Fairytale": "2_19.txt",
    "You All Over Me (feat. Maren Morris)": "2_22.txt",
    "Mr. Perfectly Fine": "2_23.txt",
    "We Were Happy": "2_24.txt",
    "That's When (feat. Keith Urban)": "2_25.txt",
    "Don't You": "2_20.txt",
    "Bye Bye Baby": "2_21.txt",
    "Mine": "3_1.txt",
    "Sparks Fly": "3_2.txt",
    "Back to December": "3_3.txt",
    "Speak Now": "3_4.txt",
    "Dear John": "3_5.txt",
    "Mean": "3_6.txt",
    "The Story of Us": "3_7.txt",
    "Never Grow Up": "3_8.txt",
    "Enchanted": "3_9.txt",
    "Better Than Revenge": "3_10.txt",
    "Innocent": "3_11.txt",
    "Haunted": "3_12.txt",
    "Last Kiss": "3_13.txt",
    "Long Live": "3_14.txt",
    "Ours": "3_15.txt",
    "Superman": "3_16.txt",
    "Electric Touch (feat. Fall Out Boy)": "3_17.txt",
    "When Emma Falls in Love": "3_18.txt",
    "I Can See You": "3_19.txt",
    "Castles Crumbling (feat. Hayley Williams)": "3_20.txt",
    "Foolish One": "3_21.txt",
    "Timeless": "3_22.txt",
    "State of Grace": "4_1.txt",
    "Red": "4_2.txt",
    "Treacherous": "4_3.txt",
    "I Knew You Were Trouble": "4_4.txt",
    "All Too Well": "4_5.txt",
    "22": "4_6.txt",
    "I Almost Do": "4_7.txt",
    "We Are Never Ever Getting Back Together": "4_8.txt",
    "Stay Stay Stay": "4_9.txt",
    "The Last Time (feat. Gary Lightbody)": "4_10.txt",
    "Holy Ground": "4_11.txt",
    "Sad Beautiful Tragic": "4_12.txt",
    "The Lucky One": "4_13.txt",
    "Everything Has Changed (feat. Ed Sheeran)": "4_14.txt",
    "Starlight": "4_15.txt",
    "Begin Again": "4_16.txt",
    "The Moment I Knew": "4_17.txt",
    "Come Back... Be Here": "4_18.txt",
    "Girl at Home": "4_19.txt",
    "State of Grace": "4_20.txt",
    "Ronan": "4_21.txt",
    "Better Man": "4_22.txt",
    "Nothing New (feat. Phoebe Bridgers)": "4_23.txt",
    "Babe": "4_24.txt",
    "Message in a Bottle": "4_25.txt",
    "I Bet You Think About Me (feat. Chris Stapleton)": "4_26.txt",
    "Forever Winter": "4_27.txt",
    "Run (feat. Ed Sheeran)": "4_28.txt",
    "The Very First Night": "4_29.txt",
    "All Too Well (10 Minute Version)": "4_30.txt"
}