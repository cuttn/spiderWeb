import { useUser } from "../components/profileContext"
import {useState, useEffect, use} from 'react'

function Profile(){
    const { currentUser } = useUser()
    const [profileData, setProfileData] = useState({name: "", type: ""})
    useEffect(() => {
        const query = async () => {
            const influencerResponse = await fetch(`http://127.0.0.1:8000/${currentUser.type}/${currentUser.id}/`);
            const influencerData = await influencerResponse.json();
            setProfileData({"name": influencerData.name, "type": "influencer"})
        }
        query();
        return;
    }, [currentUser])

    return(
        <>
        {profileData.name}
        </>
    )
}

export default Profile