import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { fetchLearnedWords } from "../redux/word";
import { addPhrase } from "../redux/phrase";
import './PhraseBuilder.css'


function PhraseBuilder() {
    const dispatch = useDispatch()
    const [learned_words, setLearnedWords] = useState([]);
    const [selectedWords, setSelectedWords] = useState([]);
    const [phrase, setPhrase] = useState('');


    useEffect(() => {
        dispatch(fetchLearnedWords())
        .then((data) => setLearnedWords(data.learned_words))
    }, []);

    console.log(learned_words)

    const handleWordSelection = (word) => {
        if (selectedWords.includes(word)) {
            setSelectedWords(selectedWords.filter((w) => w !== word))
        } else {
            setSelectedWords([...selectedWords, word])
        }
    }

    const generatePhrase = (event) => {
        event.preventDefault();
        setPhrase(selectedWords.map((word) => word.word).join('  '));
    }


    const HandleSubmit = async (event) => {
        event.preventDefault();
        const phraseData = {
            phrase
        }

        await dispatch(addPhrase(phraseData))
    } 
    return (
        <form onSubmit={HandleSubmit}>
            <div className="phrase-generator">
                <h2 className="title">Generador de oraciones</h2>
                <h3 className="info">Palabras aprendidas</h3>
                <div className="word-list-container">
                    <div className="leanerned-words-list">
                        <ul>
                            {learned_words?.map((word) => (
                                <li key={word.id} className="word-item">
                                    <label>
                                        <input
                                            type="checkbox"
                                            checked={selectedWords.includes(word)}
                                            onChange={() => handleWordSelection(word)}
                                        />
                                        {word.user_word || word.word}
                                    </label>
                                </li>
                            ))}
                        </ul>
                    </div>
                </div>
                <div className="selected-words">
                    <h1>Select palabras</h1>
                    <ul>
                        {selectedWords.map((word) => (
                            <li key={word.id}>{word.user_word || word.word}</li>
                        ))}
                    </ul>
                    <button onClick={generatePhrase}>Create</button>
                </div>
                <div className="generated-phrase">
                    <h3>Phrase:</h3>
                    <p>{phrase}</p>
                </div>
                <button type="submit">Add</button>
            </div>
        </form>
    )
}

export default PhraseBuilder