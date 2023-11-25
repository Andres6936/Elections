import {SafeAreaView, ScrollView, StatusBar, Text, useColorScheme, View} from "react-native-windows";
import {LeftNavigator} from "../layout/LeftNavigator";
import React from "react";

export function ItemsScreen() {
    const isDarkMode = useColorScheme() === 'dark';
    const backgroundStyle = "text-black bg-neutral-300 dark:bg-slate-900 dark:text-white"

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
                    <Text>
                        Hello
                    </Text>
                </ScrollView>
            </View>
        </SafeAreaView>

    )
}