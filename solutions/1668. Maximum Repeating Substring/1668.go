package main

import "strings"

func maxRepeating(sequence string, word string) int {
	var maxRepeats int
	for k := 1; k <= len(sequence)/len(word); k++ {
		if strings.Contains(sequence, strings.Repeat(word, k)) {
			maxRepeats = k
		} else {
			break
		}
	}
	return maxRepeats
}
func main() {
	sequence := "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
	println(maxRepeating(sequence, "aaba"))

}
