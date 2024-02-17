package main

func containsDuplicate(nums []int) bool {
	numMap := make(map[int]bool)
	for _, num := range nums {
		if numMap[num] {
			return true
		}
		numMap[num] = true
	}
	return false
}

func main() {
	mySlice := []int{1, 2, 3, 1}
	println(containsDuplicate(mySlice))
}
