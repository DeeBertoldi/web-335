/**
 * Daniella Bertoldi
 * Assignment 5.2 - Projections
 * Date: 02/16/2026
 */

// Add a new user
db.users.insertOne({
  firstName: "Antonio",
  lastName: "Vivaldi",
  employeeId: "1010",
  email: "vivaldi@me.com",
  dateCreated: new Date()
});

// Verify new user
db.users.find({ lastName: "Vivaldi" });

// Update Mozart's email
db.users.updateOne(
  { lastName: "Mozart" },
  { $set: { email: "mozart@me.com" } }
);

// Verify update
db.users.find({ lastName: "Mozart" });

// Display all users with projections
db.users.find(
  {},
  {
    firstName: 1,
    lastName: 1,
    email: 1,
    _id: 0
  }
);
