import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchLearnedPhrases } from "../../redux/phrase";
import { NavLink } from "react-router-dom";
import OpenModalButton from "../OpenModalButton";
import DeletePhrase from "../DeletePhrase/DeletePhrase";
import "./Phrases.css"

function PhraseTile({ learned_phrase }) {
    console.log(learned_phrase)
    return (
        <div className="">
            <NavLink to={`/learned/${learned_phrase.id}/details`} state={{ learned_phrase }} className="phrase-links">
                <div className="phrase-boxes">{learned_phrase.phrase.phrase}</div>
            </NavLink>
            <OpenModalButton
            buttonText='Delete'
            modalComponent={<DeletePhrase phrase={learned_phrase}/>}
            />
        </div>
    )
}
function LearnedPhrases() {
    const dispatch = useDispatch();
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        dispatch(fetchLearnedPhrases())
        .then(() => setLoading(false))
        .catch(() => setLoading(false))
    }, []);

    const learned = useSelector(state => state.phrase)
    console.log("PLease", learned)

    return (
        <>
        <div className="info-container">
            <h1 className="title">la frase</h1>
            <h3 className="important">Practícalos con frecuencia</h3>
            <h4>Aprende la frase</h4>
                <a href="https://www.ingles.com/" target="_blank"  rel="noreferrer" className="link">Ingles.com</a>
        </div>
        <div className="phrase-container">
            { loading ? (
                <>Loading...</>
            ) : learned && learned[0]?.phrases ? (
                learned[0].phrases?.map(lp => (
                    <PhraseTile key={lp.id} learned_phrase={lp}/>
                ))
            ) : (
                <>No frase</>
            )}
        </div>
        </>
    )
}

export default LearnedPhrases