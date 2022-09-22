package edu.gatech.seclass.quizapp;
import java.io.Serializable;
import java.sql.Timestamp;

import static edu.gatech.seclass.quizapp.MainActivity.currentUser;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Switch;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class FlashCardBackActivity extends AppCompatActivity implements Serializable {
    private TextView textView;

    private Button submitButton;
    private Button flipButton;
    private Button correctButton;
    private Button incorrectButton;
    private String frontText;
    private String backText;
    private FlashCardQuestion flashCardQuestion;
    private int correct;
    private Switch toggleSwitch;

    private boolean isAnswered;

    @Override
    protected void onCreate(Bundle savedInstanceState){
        System.out.println(currentUser);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_flashcard_back);

        textView = (TextView) findViewById(R.id.backText);
        frontText = getIntent().getExtras().getString("front");
        backText = getIntent().getExtras().getString("back");

        flashCardQuestion = (FlashCardQuestion) getIntent().getSerializableExtra("flashCard");
        isAnswered = getIntent().getExtras().getBoolean("isAnswered");

        if (isAnswered) {
            correct = getIntent().getExtras().getInt("recordedAnswer");
        }

        textView.setText(backText);
        initializeButtons();
    }

    private void initializeButtons() {
        incorrectButton = (Button) findViewById(R.id.incorrectButton);
        incorrectButton.setOnClickListener(view -> {
            markIncorrect();
            isAnswered = true;
        });

        correctButton = (Button) findViewById(R.id.correctButton2);
        correctButton.setOnClickListener(view -> {
            markCorrect();
            isAnswered= true;
        });

        submitButton = (Button) findViewById(R.id.submitButtonFB);
        submitButton.setOnClickListener(view -> {
            if (isAnswered){
                System.out.println("correct: "+correct);
                submitFunctionality();
            }
        });

        flipButton = (Button) findViewById(R.id.flipButton);
        flipButton.setOnClickListener(view -> goToFront());
        toggleSwitch = findViewById(R.id.flashcardbackswitch);
    }

    /**
     * Will record correct/incorrect based on which button was clicked before submitting
     */
    public void submitFunctionality() {
        // grade student answer
        // make user answer object, append to quiz attempt object
        System.out.println("correct: "+correct);
        Timestamp dummy  = new Timestamp(2000);
        UserAnswer userAnswer = new UserAnswer(flashCardQuestion, dummy, currentUser.userID, null, correct);

        currentUser.currentQuizAttempt.addUserAnswer(userAnswer);
        if (toggleSwitch.isChecked()) {
            currentUser.currentQuizAttempt.addToggledQuestions(flashCardQuestion);
        }
        goToNextScreen();
    }

    @Override
    public void onBackPressed () {
        return;
    }

    public void goToNextScreen() {
        int nextQ = currentUser.currentQuiz.peekNextQuestionType();
        Intent intent = new Intent(FlashCardBackActivity.this, MainActivity.class);
        System.out.println("nextQ: "+nextQ);

        if (nextQ == -1) {
            //go to main activity
            intent = new Intent(FlashCardBackActivity.this, ResultsActivity.class);
        } else if (nextQ == 1) {
            intent = new Intent(FlashCardBackActivity.this, MultipleChoiceActivity.class);
        } else if (nextQ == 2) {
            intent = new Intent(FlashCardBackActivity.this, ShortAnswerActivity.class);
        } else if (nextQ == 3) {
            // go to flashcard
            intent = new Intent(FlashCardBackActivity.this, FlashCardFrontActivity.class);
        }
        startActivity(intent);
    }

    public void goToFront() {
        Intent intent = new Intent(FlashCardBackActivity.this, FlashCardFrontActivity.class);

        intent.putExtra("front", frontText);
        intent.putExtra("back", backText);
        intent.putExtra("flashCard", flashCardQuestion);
        intent.putExtra("recordedAnswer", correct);
        intent.putExtra("isAnswered", isAnswered);
        intent.putExtra("fromBack", true);
        startActivity(intent);
    }

    public void markCorrect() {
        correct = 1;
    }

    public void markIncorrect() {
        correct = 0;
    }
}
