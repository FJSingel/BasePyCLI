#Calculates odds of no Bazaar
"""
Bazaar = 2
Powder = 1
Chaff = 0
"""
import random

def sim_hands(hands):
	results = [0,0,0,0,0,0,0,0]
	for x in xrange(0,hands):
		#Mull until bazaar	
		deck = [2,2,2,2,1,1,1,1]
		for x in xrange(0,52):
			deck.append(0)

		assert len(deck) == 60

		keep_hand = False
		hand_size = 7
		while not keep_hand:
			hand = draw_hand(deck, hand_size)
			if (2 in hand) or not hand:
				#Found a Bazaar, or empty hand
				keep_hand = True
			elif 1 not in hand:
				#Powderless Mulligan. Put hand back, draw 1 less
				deck.append(hand)
				hand_size -= 1
		results[hand_size] += 1

	print "Hand size distribution 0-7: {0}".format(results)
	hit_pct = (hands-results[0])*100/float(hands)
	print "Bazaar hit percent: {0}".format(hit_pct)

def draw_card(deck):
	choice = random.choice(deck)
	deck.remove(choice)
	return choice

def draw_hand(deck, size):
	hand = []
	for x in xrange(0,size):
		hand.append(draw_card(deck))
	return hand