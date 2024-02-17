package main

func containsNearbyDuplicate(nums []int, k int) bool {
	numMap := make(map[int]int)
	for index, num := range nums {
		if lastIndex, ok := numMap[num]; ok && index-lastIndex <= k {
			return true
		}
		numMap[num] = index
	}
	return false
}

func main() {
	mySlice := []int{1, 2, 3, 1, 2, 3}
	println(containsNearbyDuplicate(mySlice, 2))
}
