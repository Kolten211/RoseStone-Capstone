import { useDispatch } from "react-redux"
import { removePhrase } from "../../redux/phrase";
import { useModal } from "../../context/Modal";
import "./DeletePhrase.css";


function DeletePhrase({ phrase }) {
    const dispatch = useDispatch();
    const { closeModal } = useModal();

    const handleDelete = () => {
        dispatch(removePhrase(phrase.id))
        closeModal()
    };

    const handleKeep = () => {
        closeModal()
    }

    return (
        <div className="delete-modal">
            <h2>Confirm Delete</h2>
            <p>Are you sure you want to remove this phrase?</p>
            <div className="Phrase-buttons">
                <button onClick={handleDelete}>YES(Delete Phrase)</button>
                <button onClick={handleKeep} className="grayButton">No(Keep Phrase)</button>
            </div>
        </div>
    )
}

export default DeletePhrase