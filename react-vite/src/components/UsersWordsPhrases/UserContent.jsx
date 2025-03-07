import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { clearWordDetails, fetchLearnedWords } from "../../redux/word";
import OpenModalButton from "../OpenModalButton";
import "./UserContent.css"
import { NavLink } from "react-router-dom";
import DeleteWords from "../DeleteWord/DeleteWord";

function WordTile({ learned_word }) {
    console.log(learned_word)


    return (
        <div>
        <NavLink to={`/learned/${learned_word.id}/details`} state={{learned_word}} className="word-link">
            <div  className="word-boxes" >{learned_word.word}</div> 
        </NavLink>
        <OpenModalButton
        buttonText='Delete'
        modalComponent={<DeleteWords word={learned_word}/>}
        />
        </div>
    )

}
function WordBox() {
    const dispatch = useDispatch()
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        dispatch(clearWordDetails())
        dispatch(fetchLearnedWords())
        .then(() => setLoading(false))
        .catch(() => setLoading(false))
    }, []);

    const learned = useSelector(state => state.word)
    console.log('What are you?', learned)
    const learned_word = learned[0]
    console.log('What are you? 2 ', learned_word)
    const learned_array = learned_word?.learned_words
    console.log('What are you? 3 ', learned_array)
    return (
        <>
            <div className="title-info">
                <h1 className="title">Palabras aprendidas</h1>
                <h3 className="important">Asegúrate de pronunciar las palabras que has aprendido tanto como te sea posible.</h3>
                <h4>Aprende la palabra</h4>
                <a href="https://www.ingles.com/" target="_blank"  rel="noreferrer" className="link"> Ingles.com</a>
            </div>
            <div className="word-container">
                { loading ? (
                    <>Loading...</>
                ) : learned && learned[0]?.learned_words ? (
                learned[0].learned_words?.map(lw => (
                    <WordTile key={lw.id}
                    learned_word={lw} />
                )) ) : (
                    <div>No palabras</div>
                ) }
            </div>
        </>
    )
}

export default WordBox