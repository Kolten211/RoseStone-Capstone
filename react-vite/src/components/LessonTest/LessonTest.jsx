import { useState } from "react";



//{  question }
function Quiz( ) {
    const [ score, setScore ] = useState(0);
    const [ showScore, setShowScore ] = useState(false);
    const [ showText, setShowText] = useState(false);
    const [ currentQuestion, setCurrentQuestion ] = useState(0);

    const handleAnswerOptionClick = (selectedAnswer) => {
        selectedAnswer === question[currentQuestion].correctAnswer
        &&
        setScore(score + 1)
        
        const nextQuestion = currentQuestion + 1;

        if (nextQuestion < question.length) {
            setCurrentQuestion(nextQuestion);
        } else {
            setShowScore(true);
            score == question.length - 1 && setShowText(true);
        }
    };

    return (
        <div>
            <h1>Prueba de lección</h1>
            <div className="quiz-app">
                {showScore ? (
                    <div> 
                        Marcaste: {score} furea de {question.length}
                        {showText && (
                            <h4>Felicidades ¡Terminaste todas las preguntas!</h4>
                        )}
                    </div>
                ) : (
                    <>
                    <div>
                        <div>
                            <span>Pregunta {currentQuestion + 1}</span>  {/* /{questions.length} */}
                        </div>
                        <div>
                            {/* {questions[currentQuestion].question} */}
                        </div>
                    </div>
                    <div>
                        {/* {questions[currentQuestion + 1].options.map((option) => (
                            <button className="asnswer-button" key={option} onClick={handleAnswerOptionClick(option)}>
                                {option}
                            </button>
                        ))} */}
                    </div>
                    </>
                )}
            </div>
        </div>
    )

}

export default Quiz