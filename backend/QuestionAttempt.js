const mongoose = require('mongoose');

const QuestionAttemptSchema = new mongoose.Schema({
	questionId: String,
	userId: String,
	repetitions: Number,
	easeFactor: Number,
	interval: Number,
});
module.exports = mongoose.model(
	'QuestionAttempt',
	QuestionAttemptSchema,
	'QuestionAttempt'
);
