import React, {useEffect, useState} from "react";
import {Button, SafeAreaView, ScrollView, StatusBar, Text, useColorScheme, View} from "react-native-windows";
import {TypeCandidates} from "../types/TypeServices";
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

    const backgroundStyle = "text-black bg-blue-50 dark:bg-slate-900 dark:text-white"

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
                <View className="flex-row px-2 py-2 bg-white border-b border-b-indigo-200 items-center justify-between">
                    <Text className="text-black mr-3">Dashboard {">"} Candidates</Text>
                    <View className="flex-row gap-2 items-center">
                        <View className="w-[36px] h-[36px] bg-gray-600 rounded-full"></View>
                        <Text className="text-black mr-3">Joan Andrés</Text>
                    </View>
                </View>

                <ScrollView
                    contentInsetAdjustmentBehavior="automatic"
                    className={backgroundStyle}>

                    <View className="bg-white my-4 mx-4 rounded-xl shadow">
                        <View>
                            <Text className="font-bold text-lg pb-4 px-2 pt-2">Candidate Summary</Text>
                        </View>

                        <View className="bg-blue-100 flex-row gap-2 px-2 pb-2">
                            <Text className="flex-[1]">Serial</Text>
                            <Text className="flex-[3]">Candidate</Text>
                            <Text className="flex-[3]">Political Party</Text>
                        </View>

                        <View className="gap-2 my-2 px-2">
                            {candidates.map(candidate => (
                                <View key={candidate.Serial}
                                      className="flex-1 flex-row border-b border-b-gray-50 pb-2 px-2">
                                    <Text className="flex-1">{candidate.Serial}</Text>
                                    <Text className="flex-[3]">{candidate.Candidate}</Text>
                                    <Text className="flex-[3]">{candidate.PoliticalParty}</Text>
                                </View>
                            ))}
                        </View>
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