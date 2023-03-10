cartoon = input("Choose your cartoon: Frozen, Coco, Ghost, Lion king, Peter Pan : ")
quotes = ["Some people are worth melting for.", 
          "Remember me through I have to travel far.",
          "Why does everyone run away from me?",
          "Hakuna Matata, it means \"no worries for the rest of your days.\"",
          "Never grow up." ]

match cartoon:
    case "Frozen":
        print(quotes[0])
    case "Coco":
        print(quotes[1])
    case "Ghost":
        print(quotes[2])
    case "Lion king":
        print(quotes[3])
    case "Peter Pan":
        print(quotes[4])
    case _:
        print("keep trying")
