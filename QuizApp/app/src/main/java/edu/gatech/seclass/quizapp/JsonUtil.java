package edu.gatech.seclass.quizapp;

import static edu.gatech.seclass.quizapp.MainActivity.currentUser;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public final class JsonUtil {

    public static Quiz parseQuiz(JSONArray jsonArray) {
        Quiz quiz = new Quiz();
        try {
            for (int i = 0; i < jsonArray.length(); i++) {
                quiz.addQuestionToQuiz(parseQuestion(jsonArray.getJSONObject(i)));

            }
        } catch (JSONException error) {
            System.out.println("error1: " + error);
        }
        return quiz;
    }

    public static User parseUser(JSONObject jsonObject) {
        User user = new User();
        try {
            String userId = jsonObject.getString("userId");
            String password = jsonObject.getString("password");
            String name = jsonObject.getString("name");
            user.setUserID(userId);
            user.setPassword(password);
            user.setName(name);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return user;
    }

    public static JSONObject convertUser(User user) {
        JSONObject reqBody = new JSONObject();
        try {
            reqBody.put("userId", user.getUserID());
            reqBody.put("password", user.getPassword());
            reqBody.put("name", user.getName());
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return reqBody;
    }

    public static JSONObject convertQuizAttempt(QuizAttempt quizAttempt) {
        JSONObject reqBody = new JSONObject();
        try {
            reqBody.put("userId", currentUser.userID);
            reqBody.put("quizAttemptId", currentUser.currentQuizAttempt.quizAttemptID);
            reqBody.put("quizId", currentUser.currentQuizAttempt.quizID);
            reqBody.put("timeStamp", currentUser.currentQuizAttempt.timestamp);

            JSONArray jsonAnswers = new JSONArray();
            for (UserAnswer ans : currentUser.currentQuizAttempt.answers) {
                jsonAnswers.put(convertUserAnswer(ans));
            }

            reqBody.put("useranswers", jsonAnswers);
            reqBody.put("score", currentUser.currentQuizAttempt.calculateScore());
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return reqBody;
    }

    private static JSONObject convertUserAnswer(UserAnswer ans) {
        JSONObject jans = new JSONObject();
        try {
            jans.put("questionId", ans.getQuestionID());
            jans.put("answerText", ans.getAnswerText());
            jans.put("timeStamp", ans.getTimestamp());
            jans.put("topic", ans.getTopic());
            jans.put("score", ans.getScore());
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return jans;
    }

    private static Question parseQuestion(JSONObject jsonObject) {
        try {
            int questionType = jsonObject.getInt("questionType");
            String questionId = jsonObject.getString("questionId");
            int quizId = jsonObject.getInt("quizId");
            String questionText = jsonObject.getString("questionText");
            String correctAnswer = jsonObject.getString("correctAnswer");
            String topic = jsonObject.getString("topic");
            String backText = jsonObject.getString("backText");
            String hint = jsonObject.getString("hint");
            ArrayList<String> incorrectChoices = new ArrayList<>();
            for (int i = 0; i < jsonObject.getJSONArray("incorrectChoices").length(); i++) {
                incorrectChoices.add(jsonObject.getJSONArray("incorrectChoices").getString(i));
            }

            // mc
            if (questionType == 1) {
                System.out.println(questionId + ": im a mcq");
                MultipleChoiceQuestion mcq = new MultipleChoiceQuestion(questionId, quizId, questionText, hint);
                mcq.setTopic(topic);
                mcq.setIncorrectChoices(incorrectChoices);
                mcq.setCorrectAnswer(correctAnswer);
                mcq.setHint(hint);
                return mcq;
            }
            //sa
            else if (questionType == 2) {
                System.out.println(questionId + ": im a saq");
                ShortAnswerQuestion saq = new ShortAnswerQuestion(questionId, quizId, questionText, hint);
                saq.setTopic(topic);
                saq.setCorrectAnswer(correctAnswer);
                saq.setHint(hint);
                return saq;
            } else if (questionType == 3) {
                System.out.println(questionId + ": im a faq");
                //flashcard
                FlashCardQuestion faq = new FlashCardQuestion(questionId, quizId, questionText, hint);
                faq.setBackOfCard(backText);
                faq.setTopic(topic);
                faq.setHint(hint);
                return faq;
            }
        } catch (JSONException error) {
            System.out.println(error);
        }
        return null;
    }
}
