from cow import Cow
import sys


def get_cows():
    cow_names = ["heifer", "kitteh"]

    quote_lines = "    \\\n"
    quote_lines += "     \\\n"
    quote_lines += "      \\\n"

    cow_images = [
        "        ^__^\n"
        + "        (oo)\\_______\n"
        + "        (__)\\       )\\/\\\n"
        + "            ||----w |\n"
        + "            ||     ||\n",
        "       (\"`-'  '-/\") .___..--' ' \"`-._\n"
        + "         ` *_ *  )    `-.   (      ) .`-.__. `)\n"
        + "         (_Y_.) ' ._   )   `._` ;  `` -. .-'\n"
        + "      _.. `--'_..-_/   /--' _ .' ,4\n"
        + "   ( i l ),-''  ( l i),'  ( ( ! .-'\n",
    ]
    cows = [None] * len(cow_images)
    for index in range(len(cows)):
        cows[index] = Cow(cow_names[index])
        cows[index].set_image(quote_lines + cow_images[index])
    return cows


def list_cows(cows):   #Cows available: heifer kitteh
    print("Cows available:", end = " ")
    for cow in cows:
        print(cow.get_name(), end = " ")


def find_cow(name, cows):
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None



def main():
    cows = get_cows()

    if len(sys.argv) == 2 and sys.argv[1] == "-l":  #List all cows
        list_cows(cows)


    elif len(sys.argv) >= 4 and sys.argv[1] == "-n":        #print message w/ specific cow
        cow_name = sys.argv[2].lower()
        message = " ".join(sys.argv[3:])
        cow = find_cow(cow_name, cows)
        if cow:
            print(message)
            print(cow.get_image())
        else:
            print(f"Could not find {cow_name} cow!")


    elif len(sys.argv) >= 2:    #print message w/ default cow
        message = " ".join(sys.argv[1:])
        default_cow = cows[0]
        print(message)
        print(default_cow.get_image())


if __name__ == "__main__":
    main()
