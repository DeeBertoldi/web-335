/**
 * Name: Daniella Bertoldi
 * Assignment: Exercise 4.3 – MongoDB Shell
 * Date: 02/08/2026
 * Description: MongoDB queries for the users collection
 */

// Display all users in the collection
db.users.find();

// ser with the email address jbach@me.com
db.users.findOne({ email: "jbach@me.com" });

// user with the last name Mozart
db.users.findOne({ lastName: "Mozart" });

// user with the first name Richard
db.users.findOne({ firstName: "Richard" });

// user with employeeId 1010
db.users.findOne({ employeeId: "1010" });
