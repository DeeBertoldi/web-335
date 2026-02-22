mongosh "mongodb+srv://bellevueuniversity.llngijj.mongodb.net/" --apiVersion 1 --username web335_admin

use web335

load("houses.js")

db.students.find();

newStudent = {
  firstName: "Daniella",
  lastName: "Bertoldi",
  studentId: "s2000",
  houseId: "h1009"
};
db.students.insertOne(newStudent);

db.students.findOne({ studentId: "s2000" });

db.students.updateOne(
  { studentId: "s2000" },
  { $set: { lastName: "Nova" } }
);

db.students.findOne({ studentId: "s2000" });

db.students.deleteOne({ studentId: "s2000" });

db.students.findOne({ studentId: "s2000" });

db.houses.aggregate([
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students"
    }
  }
]);

db.houses.aggregate([
  { $match: { founder: "Godric Gryffindor" } },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students"
    }
  }
]);

db.houses.aggregate([
  { $match: { mascot: "Eagle" } },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students"
    }
  }
]);