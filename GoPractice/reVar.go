package main

import "fmt"

func main() {
	constVar := "I do not change"
	const stable int = 10
	var smallInt int32
	var bigInt int64 = 1361416
	fmt.Printf("constVar %s & stable %s\n", constVar, "new")
	fmt.Printf("smallInt %d & bigInt %d\n", smallInt, bigInt)
}
