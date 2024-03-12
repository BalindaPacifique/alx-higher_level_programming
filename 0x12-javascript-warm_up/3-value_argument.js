#!/usr/bin/node

if (process.agrv == undefined) {
	console.log("No argument");
} else {
	console.log(process.argv);
}
