import React, {useEffect, useState} from 'react';
import {SafeAreaView, ScrollView, StatusBar, Text, useColorScheme, View,} from 'react-native';
import {CandidateService} from "./src/services/CandidateService";
import {TypeCandidates} from "./src/types/TypeCandidates";


function App(): JSX.Element {
    const isDarkMode = useColorScheme() === 'dark';
    const [candidates, setCandidates] = useState<TypeCandidates[]>([])

    useEffect(() => {
        (async () => {
            const candidateService = new CandidateService();
            const candidates = await candidateService.getAllCandidates();
            setCandidates(candidates)
        })()
    }, []);

    const backgroundStyle = "text-black bg-neutral-300 dark:bg-slate-900 dark:text-white"

    return (
        <SafeAreaView className={"flex-1"}>
            <StatusBar
                barStyle={isDarkMode ? 'light-content' : 'dark-content'}
            />
            <ScrollView
                contentInsetAdjustmentBehavior="automatic"
                className={backgroundStyle}>
                <View className="bg-white dark:bg-black p-2 gap-2">
                    {candidates.map(candidate => (
                        <View key={candidate.Serial} className="flex flex-1 border border-sky-500">
                            <Text>Candidate: {candidate.Candidate}</Text>
                            <Text>Political Party: {candidate.PoliticalParty}</Text>
                        </View>
                    ))}
                </View>
            </ScrollView>
            <View className="p-2 bg-white border-t-4 border-indigo-500">
                <Text className="text-black">Show: 0 of 25 registers</Text>
            </View>
        </SafeAreaView>
    );
}

export default App;
