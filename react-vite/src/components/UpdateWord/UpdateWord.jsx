import { useEffect, useState } from "react"
import { useDispatch } from "react-redux"
import { editWord } from "../../redux/word";
import VoiceRecorder from "./Recorder";
import { useLocation, useParams } from "react-router-dom";



function UpdateWord() {
    const dispatch = useDispatch();
    // const navigate = useNavigate();
    const {word_id} = useParams();
    const location = useLocation();
    const { learned_word }= location.state
    console.log("WordData", learned_word)

    const [audioBlob, setAudioBlob] = useState("")
    const [part_of_speech, setPartOfSpeech] = useState("")
    const [translation, setTranslation] = useState("")
    const [word, setWord] = useState("")

    useEffect(() => {
        if (learned_word) {
            setAudioBlob(learned_word.audio)
            setPartOfSpeech(learned_word.part_of_speech)
            setTranslation(learned_word.translation)
            setWord(learned_word.word)
        }
    }, []);

    // const validateForm = () => {
    //     let isValid = true; 

    //     return isValid
    // }

    const handleAudioRecorded = (blob) => {
        setAudioBlob(blob)
    }

    const handleSubmit = async (event) => {
        event.preventDefault()

        // if (validateForm) {
        //     const wordData ={
        //         id: word_id,
        //         audioBlob,
        //         part_of_speech,
        //         translation,
        //         word
        //     }
        const wordData = new FormData();
        console.log('passing', wordData)
        if (audioBlob) {
            wordData.append('audio', audioBlob, 'recording.wav')
        }
        wordData.append('translation', translation);
        wordData.append('part_of_speech', part_of_speech);
        wordData.append('word', word)
        console.log('audio added?', wordData )
        for (let [key, value] of wordData.entries()) {
            console.log(key, value);
        }
        await dispatch(editWord({ id: word_id, wordData}));
    }
    return (
        <form onSubmit={handleSubmit}>
            <h1 className="title">Actualizar palabra</h1>
            <h3>Puedes añadir una grabación de ti diciendo la palabra</h3>
            <label className="word-label">Learned palabra</label><p>{learned_word.word}</p>
            <label className="audio">Audio
               <VoiceRecorder onAudioRecorded={handleAudioRecorded} />
            </label>
            <label>
                Traducción
                <input
                    type="text"
                    name="translation"
                    value={translation}
                    onChange={(e) => setTranslation(e.target.value)}
                    placeholder="translation"
                />
            </label>
            <label>
                Categorías gramaticales
                <input
                    type="text"
                    name="part_of_speech"
                    value={part_of_speech}
                    onChange={(e) => setPartOfSpeech(e.target.value)}
                    placeholder="Part of speech"
                />
            </label>
            <label>
                Word
                <input 
                    type="text"
                    name="user_word"
                    value={word}
                    onChange={(e) => setWord(e.target.value)}
                    placeholder="Palabra"
                />
           </label>
            <button type="submit">Create</button>
        </form>
    )
}

export default UpdateWord