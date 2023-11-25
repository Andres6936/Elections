import React, {useEffect, useState} from "react";
import {Button, SafeAreaView, ScrollView, StatusBar, Text, useColorScheme, View} from "react-native-windows";
import {TypeCandidates} from "../types/TypeCandidates";
import {CandidateService} from "../services/CandidateService";
import {LeftNavigator} from "../layout/LeftNavigator";

export function CandidateScreen() {
    const isDarkMode = useColorScheme() === 'dark';
    const [isPaginationEnd, setIsPaginationEnd] = useState<boolean>(false)
    const [isError, setIsError] = useState([false, "Not Error"])
    const [currentPage, setCurrentPage] = useState<number>(0)
    const [pageSize, setPageSize] = useState<number>(60);
    const [candidates, setCandidates] = useState<TypeCandidates[]>([])

    useEffect(() => {
        (async () => {
            try {
                if (isPaginationEnd) return;

                const candidateService = new CandidateService();
                const candidates = await candidateService.getAllCandidates({
                    skip: currentPage,
                    limit: pageSize,
                });
                // If the results of endpoint are lesser that the required for the pageSize, reach the page end
                if (candidates.length < pageSize) setIsPaginationEnd(true)

                setCandidates(candidates)
            } catch (exception) {
                setIsError([true, "Promise Rejected"])
            }
        })()
    }, [currentPage, pageSize, isPaginationEnd]);

    const backgroundStyle = "text-black bg-neutral-300 dark:bg-slate-900 dark:text-white"

    const previousPage = () => {
        if (currentPage >= 1) {
            setCurrentPage(currentPage - 1)
        }
    }

    const nextPage = () => {
        if (isPaginationEnd) return

        setCurrentPage(currentPage + 1)
    }

    return (
        <SafeAreaView className={"flex-1 flex-row bg-white"}>
            <StatusBar
                barStyle={isDarkMode ? 'light-content' : 'dark-content'}
            />
            <LeftNavigator/>
            <View className="flex-[9] border-l">
                <ScrollView
                    contentInsetAdjustmentBehavior="automatic"
                    className={backgroundStyle}>
                    <View className="bg-white dark:bg-black p-2 gap-2">
                        {candidates.map(candidate => (
                            <View key={candidate.Serial} className="flex-1 border border-red-200 rounded p-2">
                                <Text className="font-bold text-md">Candidate: {candidate.Candidate}</Text>
                                <Text>Political Party: {candidate.PoliticalParty}</Text>
                                <View className="flex-row mt-2">
                                    <Button className="w-24 bg-sky-500" title="Edit"></Button>
                                    <Button className="w-24 bg-red-500" title="Delete"></Button>
                                </View>
                            </View>
                        ))}
                    </View>
                </ScrollView>
                <View className="flex-row p-2 bg-white border-t border-indigo-500 items-center">
                    <Text className="text-black mr-3">Show: {pageSize} registers of {currentPage + 1} page</Text>
                    <Button onPress={previousPage} disabled={currentPage === 0} className="bg-blue-500 text-black"
                            title="Prev">Prev</Button>
                    <Button onPress={nextPage} disabled={isPaginationEnd} className="bg-blue-500 text-black"
                            title="Next">Next</Button>
                </View>
            </View>
        </SafeAreaView>
    )
}