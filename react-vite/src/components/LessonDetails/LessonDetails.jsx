import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { clearLessonDetails, fetchLessonDetails, finishedLesson } from '../../redux/lesson';
import './LessonDetails.css'

function LessonDetails() {
    const { lesson_id } = useParams();
    const dispatch = useDispatch();
    // const [userlesson, setlesson] = useState(null)
    const [showTest, setShowTest] = useState(false)
    // const [ userAnswers, setUserAnswers ] = useState({})

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

    // const handleSubmit = () => {
    //     dispatch(finishedLesson())

       
    // }

    return (
        <div className='details-container'>
            <div>
                <h2 className='lesson-title'>{lessonDetails?.title}</h2>
            </div>
            <div>
                <p className='lesson-creator'>Creado por: {lessonDetails?.user_id}</p>
                <p className='lesson-creator'>La dificultad: {lessonDetails?.difficulty}</p>
                <p className='lesson-creator'>La descripción: {lessonDetails?.description}</p>
            </div>
            <div >
                <h3 className='lesson-name'>La palabra</h3>
            </div>
            <div className={lessonDetails?.words ? "foo-present" : "foo-absent"}>
                <div>
                    {lessonDetails?.words?.map((word) => (
                        <h4 key={word.id}>{word.word}</h4>
                    ))}
                </div>
            </div>
            <h3 className='lesson-h3'>La frase</h3>
            <div className={lessonDetails?.phrases.length > 0 ? "foo-present" : "foo-absent"}>
                <div className='list'>
                    {lessonDetails?.phrases?.map((phrase) => (
                        <h4 key={phrase.id} >{phrase.phrase}</h4>
                    ))}
                </div>
            </div>
            <button onClick={handleStart}>Iniciar prueba</button>

            {showTest && (
                <div>
                    <h2 className='lesson-title'>Test</h2>
                    <h3 className='lesson-h3'>Feature coming soon / Función próximamente </h3>
                </div>
            )}
        </div>
    )
}


export default LessonDetails