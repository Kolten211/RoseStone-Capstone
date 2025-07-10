import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import { fetchQuestions, finishedLesson } from "../../redux/lesson";



//{  question }
function Quiz( ) {
    const {lesson_id} = useParams();
    const dispatch = useDispatch();
    const [ score, setScore ] = useState(0);
    const [ userSelection, setSelection ] = useState({});
    const [ quizSubmitted, setQuizSubmitted ] = useState(false);
    // const [ showText, setShowText ] = useState(false);
    const [ showResult, setShowResult ] = useState(false);
    const [ currentQuestion, setCurrentQuestion ] = useState(0);
    const navigate = useNavigate();


    useEffect(() => {
        dispatch(fetchQuestions(lesson_id))
    }, []);

    const data = useSelector(state => state.lesson);
    // const questions = useSelector(state => state.questions);
    const questions = data.questions
    console.log("what I need", questions)
    
    const handleAnswerOptionClick = (question_id, answer_id) => {
        setSelection(prevSelection => ({
            ...prevSelection,
            [question_id]: answer_id
        }))
        // selectedAnswer === question[currentQuestion].correctAnswer
        // &&
        // setScore(score + 1)
        
        // const nextQuestion = currentQuestion + 1;

        // if (nextQuestion < question.length) {
        //     setCurrentQuestion(nextQuestion);
        // } else {
        //     setShowScore(true);
        //     score == question.length - 1 && setShowText(true);
        // }

    };
    const handleNextQuestion = () => {
        const nextQuestion = currentQuestion + 1;
        if (nextQuestion < questions.length) {
            setCurrentQuestion(nextQuestion);
        } else {
            setShowResult(true)
        }
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        setQuizSubmitted(true);
        console.log("answers", userSelection)
        const lessonData = {
            id: lesson_id,
            userSelection: userSelection
        }
        
        
        const result = await dispatch(finishedLesson(lessonData));

        if(result && !result.errors) {
            console.log("Quiz Result", result)
            setScore(result.score)
            setShowResult(true)
        }else {
            console.error("Error occured", result.error)
        }
        
    }
    

    if (!questions?.length) {
        return <div>Cargando preguntas...</div>
    }

    

    if (data.error) {
        return <div>Error al cargar el cuestionario: {data.error.message || 'Unknown error'}</div>
    }

    const question = questions[currentQuestion];
    const selectedAnswer = userSelection[question?.id];

    console.log("QUESTIONS?", questions)
    console.log("ANSWERS?", question.answers)
    console.log("RESULT", data)
    
    if (!question) {
        return <div>No se pudo cargar la pregunta actual.</div>
    }
    return (
        <div>
            <h1>Prueba de lección</h1>
            <div className="quiz-app">
                {!showResult ? (
                    <form onSubmit={handleSubmit}>
                        <div>
                            <div>
                                <span>Pregunta {currentQuestion + 1}</span>
                            </div>
                            <div>
                                {question.question_text}
                            </div>
                        </div>
                        <div>
                            {question.answers?.map((answer) => (
                                <button
                                    type="button"
                                    className=""
                                    key={answer.id}
                                    onClick={() => handleAnswerOptionClick(question.id, answer.id)}
                                >
                                    {answer.answer_text}
                                </button>
                            ))}
                        </div>
                        <div>
                            {currentQuestion < questions?.length - 1 && (
                                <button
                                type="button"
                                onClick={handleNextQuestion}
                                disabled={!selectedAnswer}>
                                    Siguiente Pregunta
                                </button>
                            )}
                            {currentQuestion === questions.length - 1 && (
                                <button
                                type="submit"
                                disabled={!selectedAnswer}>
                                    Enviar Cuestionario
                                </button>
                            )}
                        </div>
                    </form>
                    
                ) : (
                    <div> 
                        {/* <p>Marcaste: {score}% furea de {questions.length}</p> */}
                        
                        <p>Tu puntuación: <strong>{score.toFixed(2)}%</strong></p>
                        <h4>Felicidades ¡Terminaste todas las preguntas!</h4>
                        <button
                        type="button"
                        onClick={() => navigate('/landing-page')}>
                            Volver a Lecciones
                        </button>
                       
                    </div>
                    // <>
                    // <div>
                    //     <div>
                    //         <span>Pregunta {currentQuestion + 1}</span>  /{questions.length}
                    //     </div>
                    //     <div>
                    //         {/* {questions[currentQuestion].question} */}
                    //     </div>
                    // </div>
                    // <div>
                    //     {questions[currentQuestion + 1].options.map((option) => (
                    //         <button className="asnswer-button" key={option} onClick={handleAnswerOptionClick(option)}>
                    //             {option}
                    //         </button>
                    //     ))}
                    // </div>
                    // </>
                )}
            </div>
        </div>
    )

}

export default Quiz