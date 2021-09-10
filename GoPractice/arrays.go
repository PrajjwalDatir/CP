package main

import "fmt"

func main() {
	/* Define an array of size 4 that stores deployment options */
	var DeploymentOptions = [3]string{"1st", "2nd", "3rd"}

	/* Loop through the deployment options array */
	for i := 0; i < len(DeploymentOptions); i++ {
		fmt.Printf("Index %d: Element %s \n", i+1, DeploymentOptions[i])
	}
}
