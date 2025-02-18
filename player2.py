name = input("name your player")

match name:
    case "ronaldo" | "ozil" | "R9" | "modric" | "kroos" | "zidane" | "beckam":
        print("real madrid")
    case "messi" | "ronaldinho" | "etoo" | "iniesta" | "xavi" :
        print("barcelona")
    case _ :
        print("other good clubs")