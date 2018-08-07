from itertools import product, permutations


class song: # define the attributes for each song
    def __init__(self, name, singer, quiet, cover):
        self.name = name
        self.singer = singer
        self.quiet = quiet
        self.cover = cover


Songs = [] # initiate list of songs and their attributes
Songs.append(song("Your Love Is A Dumpster Fire","Tal", False, False))
Songs.append(song("Wayward", "Tal", False, False))
Songs.append(song("Grounded","Luke", True, True))
Songs.append(song("Sinister Vistas", "Mike", True, False))
Songs.append(song("Imposter Sun","Luke", False, False))
Songs.append(song("Turnaround","Mike", False, False))
Songs.append(song("Honeycomb","Tal", False, False))
Songs.append(song("Play Dead", "Tal", True, False))


def printallorders(all_my_orders): # print all current setlist possibilities in an eye pleasing way
    for permutation in all_my_orders:
        for each_song in permutation:
            print permutation.index(each_song)+1, each_song.name

def check_if_dumpster_first(setlist): # band has decided this song is first, so all setlists must comply
    correct_setlists = [x for x in setlist if x[0].name == "Your Love Is A Dumpster Fire"]
    return correct_setlists

def check_if_play_dead_last(setlist): # band has decided this song is last, so all setlists must comply
    correct_setlists = [x for x in setlist if x[7].name == "Play Dead"]
    return correct_setlists

def check_if_honeycomb_not_second(setlist): # this song must not be second
    correct_setlists = [x for x in setlist if x[1].name != "Honeycomb"]
    return correct_setlists


def check_if_too_quiet(setlist): # do not have 2 songs which are "quiet" after one another in setlist
    correct_setlists = [x for x in setlist if not(too_quiet(x))]
    return correct_setlists

def too_quiet(setlist): # are there 2 songs with quiet == True next to each other?
    for i in xrange(len(setlist)-1):
        if (setlist[i].quiet and setlist[i+1].quiet):
            return True
    return False

def turner(setlist): # this song must be second
    setlists = [x for x in setlist if x[1].name == "Turnaround"]
    return setlists

def ringofied(setlist): # is there a ringo moment in the set? where one of the other singers
    # sings both his songs back to back?
    for i in xrange(len(setlist) - 1):
        if setlist[i].singer == setlist[i+1].singer and setlist[i].singer != "Tal":
            return True
    return False


def check_no_ringo(setlist): # don't let a ringo moment happen in the set
    correct_setlists= []
    correct_setlists = [x for x in setlist if not ringofied(x)]
    return correct_setlists



def cover_in_second_half(setlist): # the one cover we have in the set, should be in the second half of our set
    correct_setlists = []
    correct_setlists = [x for x in setlist if ( not x[0].cover and not x[1].cover and not x[2].cover and not x[3].cover )]
    return correct_setlists

#execution of the functions here:

allorders = permutations(Songs, 8) #find all set list
cluster = list(allorders) # order them as a list
print "all possibilities"
print len(cluster)
g = check_if_dumpster_first(cluster)
print "after making sure your love is first"
print len(g)
print "after making sure play dead is last"
s = check_if_play_dead_last(g)
print len(s)
f = check_if_honeycomb_not_second(s)
print "after making sure honeycomb is not second"
print len(f)

u = cover_in_second_half(f)

print "after making sure pavement cover is in second half of the show"
print len(u)
y = check_no_ringo(u)
print("after ringo check")
print len(y)


end = check_if_too_quiet(y)
print "after making sure no 2 quiet songs in a row"
print len(end)
ender = turner(end)
"turnaround second song"
print len(ender)
print "now results"
printallorders(ender)



