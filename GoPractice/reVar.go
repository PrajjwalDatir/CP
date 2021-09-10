package main

import "fmt"

func main() {
	constVar := "I do not change"
	const stable int = 10

	fmt.Println(constVar, stable)
}
