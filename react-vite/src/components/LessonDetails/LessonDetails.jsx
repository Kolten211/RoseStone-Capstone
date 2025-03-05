import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { clearLessonDetails, fetchLessonDetails, finishedLesson } from '../../redux/lesson';


function LessonDetails() {
    const { lesson_id } = useParams();
    const dispatch = useDispatch();
    const [userlesson, setlesson] = useState(null)
    const [showTest, setShowTest] = useState(false)
    const [ userAnswers, setUserAnswers ] = useState({})

    useEffect(() => {
        dispatch(clearLessonDetails())
        dispatch(fetchLessonDetails(lesson_id))

        // const generateQuestions = lesson.words.map((word) => ({
        //     id: word.id,
        //     question: `Qué escuchas`
        // }))
    }, []);

    
    const lesson = useSelector(state => state.lesson)

    console.log(lesson)
    const lessonDetails = lesson[0]

    console.log("details", lessonDetails)

    const handleStart = () => {
        setShowTest(true);
    }

    console.log("Am i understanding you", lesson)

    const handleSubmit = () => {
        dispatch(finishedLesson())

       
    }

    return (
        <>
            <div>
                <h2>{lessonDetails?.title}</h2>
            </div>
            <div>
                <p>Creado por: {lessonDetails?.user_id}</p>
                <p>La dificultad: {lessonDetails?.difficulty}</p>
                <p>La descripción: {lessonDetails?.description}</p>
            </div>
            <div>
                <h3>La palabra</h3>
            </div>
            <ul>
                {lessonDetails?.words?.map((word) => (
                    <li key={word.id}>{word.word}</li>
                ))}
            </ul>
            <h3>La frase</h3>
            <ul>
                {lessonDetails?.phrases?.map((phrase) => (
                    <li key={phrase.id}>{phrase.phrase}</li>
                ))}
            </ul>
            <button onClick={handleStart}>Iniciar prueba</button>

            {showTest && (
                <div>
                    <h2>Test</h2>
                    <ul>
                        {}
                    </ul>
                </div>
            )}
        </>
    )
}


export default LessonDetails