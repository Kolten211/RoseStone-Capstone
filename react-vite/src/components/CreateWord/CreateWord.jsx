import { useState } from "react";
import { useDispatch } from "react-redux";
import { addWord } from "../../redux/word";
import { useNavigate } from "react-router-dom";


function CreateWord() {
    const dispatch = useDispatch();
    const navigate = useNavigate()

    const [word, setWord] = useState('');
    const [translation, setTranslation] = useState('');
    const [errors, setErrors] = useState({})

    const validateForm = () => {
        const newErrors = {};

        if (!word) {
            newErrors.word = 'Debes tener una palabra'
        }

        if (!translation) {
            newErrors.translation = 'Traducción al español de la palabra'
        }

        if (Object.keys(newErrors).length > 0) {
            setErrors(newErrors);
            return false
        }
        setErrors(newErrors)
        return true
    }

    const handleSubmit = async (event) => {
        event.preventDefault()

        if (validateForm()) {
            const wordData = {
                word,
                translation
            }

            await dispatch(addWord(wordData))

            navigate('/learned-words')
        }
    }

    return (
        <form onSubmit={handleSubmit} className="createWordForm">
            <h1> Crea una palabra </h1>
            <h3>¿Qué palabra aprendiste?</h3>
            <div>
                <label className="create-label">la palabra
                    <input 
                        type="text"
                        id="word"
                        value={word}
                        onChange={(e) => setWord(e.target.value)}
                        className="create-input"
                        placeholder="Palabra"
                    />
                    {errors.word && <p className="errors">{errors.word}</p>}
                </label>
            </div>
            <div>
                <label className="create-label"> la traducción
                    <input 
                        type="text"
                        id="tanslation"
                        value={translation}
                        onChange={(e) => setTranslation(e.target.value)}
                        className="create-input"
                        placeholder="Traducción"
                    />
                    {errors.translation && <p className="errors">{errors.translation}</p>}
                </label>
            </div>
            <button type="submit" className="create-button">Crea tu palabra</button>
        </form>
    )

}

export default CreateWord