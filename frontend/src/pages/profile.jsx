import { useUser } from "../components/profileContext"

function Profile(){
    const { currentUser } = useUser()
    return(
        <>
        {currentUser.name}
        </>
    )
}

export default Profile