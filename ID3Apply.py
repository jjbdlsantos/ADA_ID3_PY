
def runDecisionTree(df, x):
    if df.iloc[x]['odor'] == 'a' or df.iloc[x]['odor'] == 'l':
        return 'e'
    if df.iloc[x]['odor'] == 'c' or df.iloc[x]['odor'] == 'f' or df.iloc[x]['odor'] == 'p' or df.iloc[x]['odor'] == 's' or df.iloc[x]['odor'] == 'y':
        return 'p'
    if df.iloc[x]['odor'] == 'n':
        if df.iloc[x]['spore-print-color'] == 'w':
            if df.iloc[x]['habitat'] == 'd' or df.iloc[x]['habitat'] == 'g' or df.iloc[x]['habitat'] == 'm' or df.iloc[x]['habitat'] == 'p' or df.iloc[x]['habitat'] == 'w':
                return 'e'
            if df.iloc[x]['habitat'] == 'l' or df.iloc[x]['habitat'] == 'u':
                return 'p'
        if df.iloc[x]['spore-print-color'] == 'k' or df.iloc[x]['spore-print-color'] == 'n':
            if df.iloc[x]['gill-size'] == 'b':
                return 'e'
            if df.iloc[x]['gill-size'] == 'n':
                return 'p'
        if df.iloc[x]['spore-print-color'] == 'r':
            return 'p'
        if df.iloc[x]['spore-print-color'] == 'u':
            return 'e'
        if df.iloc[x]['spore-print-color'] == 'h':
            if df.iloc[x]['stalk-root'] == '?':
                if df.iloc[x]['gill-color'] == 'b' or df.iloc[x]['gill-color'] == 'k' or df.iloc[x]['gill-color'] == 'k':
                    return 'p'
                if df.iloc[x]['gill-color'] == 'e' or df.iloc[x]['gill-color'] == 'g' or df.iloc[x]['gill-color'] == 'h' or df.iloc[x]['gill-color'] == 'n' or df.iloc[x]['gill-color'] == 'u' or df.iloc[x]['gill-color'] == 'w':
                    return 'e'
            if df.iloc[x]['stalk-root'] == 'e':
                if df.iloc[x]['bruises'] == 't':
                    return 'p'
                if df.iloc[x]['bruises'] == 'f':
                    return 'e'
            if df.iloc[x]['stalk-root'] == 'r' or df.iloc[x]['stalk-root'] == 'c':
                return 'e'
            if df.iloc[x]['stalk-root'] == 'b':
                if df.iloc[x]['stalk-shape'] == 't':
                    if df.iloc[x]['habitat'] == 'd' or df.iloc[x]['habitat'] == 'g' or df.iloc[x]['habitat'] == 'm' or df.iloc[x]['habitat'] == 'p' or df.iloc[x]['habitat'] == 'w':
                        return 'e'
                    if df.iloc[x]['habitat'] == 'l' or df.iloc[x]['habitat'] == 'u':
                        return 'p'
                if df.iloc[x]['stalk-shape'] == 'e':
                    if df.iloc[x]['stalk-surface-below-ring'] == 'f':
                        if df.iloc[x]['ring-type'] == 'e' or df.iloc[x]['ring-type'] == 'f':
                            return 'e'
                        if df.iloc[x]['ring-type'] == 'p' or df.iloc[x]['ring-type'] == 'l':
                            return 'p'
                    if df.iloc[x]['stalk-surface-below-ring'] == 'k':
                        return 'p'
                    if df.iloc[x]['stalk-surface-below-ring'] == 's':
                        if df.iloc[x]['gill-size'] == 'b':
                            return 'e'
                        if df.iloc[x]['gill-size'] == 'n':
                            return 'p'
                    if df.iloc[x]['stalk-surface-below-ring'] == 'y':
                        if df.iloc[x]['stalk-color-below-ring'] == 'w':
                            if df.iloc[x]['gill-size'] == 'b':
                                return 'e'
                            if df.iloc[x]['gill-size'] == 'n':
                                return 'p'
                        if df.iloc[x]['stalk-color-below-ring'] == 'p':
                            if df.iloc[x]['ring-type'] == 'e' or df.iloc[x]['ring-type'] == 'f':
                                return 'e'
                            if df.iloc[x]['ring-type'] == 'p' or df.iloc[x]['ring-type'] == 'l':
                                return 'p'
                        if df.iloc[x]['stalk-color-below-ring'] == 'e' or df.iloc[x]['stalk-color-below-ring'] == 'g':
                            return 'e'
                        if df.iloc[x]['stalk-color-below-ring'] == 'b' or df.iloc[x]['stalk-color-below-ring'] == 'k' or df.iloc[x]['stalk-color-below-ring'] == 'y':
                            return 'p'
                        if df.iloc[x]['stalk-color-below-ring'] == 'n':
                            if df.iloc[x]['habitat'] == 'u':
                                if df.iloc[x]['bruises'] == 't':
                                    return 'p'
                                if df.iloc[x]['bruises'] == 'p' or df.iloc[x]['bruises'] == 'u':
                                    return 'e'
                            if df.iloc[x]['habitat'] == 'l':
                                if df.iloc[x]['cap-shape'] == 'x':
                                    return 'p'
                                if df.iloc[x]['cap-shape'] == 's' or df.iloc[x]['cap-shape'] == 'b' or df.iloc[x]['cap-shape'] == 'k' or df.iloc[x]['cap-shape'] == 'f':
                                    return 'e'
                            if df.iloc[x]['habitat'] == 'm':
                                if df.iloc[x]['population'] == 'a' or df.iloc[x]['population'] == 'c' or df.iloc[x]['population'] == 'n' or df.iloc[x]['population'] == 'y':
                                    return 'e'
                                if df.iloc[x]['population'] == 's' or df.iloc[x]['population'] == 'v':
                                    return 'p'                                
                            if df.iloc[x]['habitat'] == 'g' or df.iloc[x]['habitat'] == 'p':
                                if df.iloc[x]['ring-type'] == 'e' or df.iloc[x]['ring-type'] == 'f':
                                    return 'e'
                                if df.iloc[x]['ring-type'] == 'p' or df.iloc[x]['ring-type'] == 'l':
                                    return 'p' 
                            if df.iloc[x]['habitat'] == 'w':
                                return 'e'
                            if df.iloc[x]['habitat'] == 'd':
                                if df.iloc[x]['bruises'] == 'f':
                                    if df.iloc[x]['ring-type'] == 'e' or df.iloc[x]['ring-type'] == 'f':
                                        return 'e'
                                    if df.iloc[x]['ring-type'] == 'p' or df.iloc[x]['ring-type'] == 'l':
                                        return 'p'   
                                if df.iloc[x]['bruises'] == 't':
                                    if df.iloc[x]['gill-size'] == 'n':
                                        if df.iloc[x]['population'] == 'a' or df.iloc[x]['population'] == 'c' or df.iloc[x]['population'] == 'n' or df.iloc[x]['population'] == 'y':
                                            return 'e'
                                        if df.iloc[x]['population'] == 's' or df.iloc[x]['population'] == 'v':
                                            return 'p'
                                    if df.iloc[x]['gill-size'] == 'b':
                                        if df.iloc[x]['stalk-surface-above-ring'] == 'f':
                                            if df.iloc[x]['ring-type'] == 'e' or df.iloc[x]['ring-type'] == 'f':
                                                return 'e'
                                            if df.iloc[x]['ring-type'] == 'p' or df.iloc[x]['ring-type'] == 'l':
                                                return 'p'                                           
                                        if df.iloc[x]['stalk-surface-above-ring'] == 'k':
                                            return 'p'
                                        if df.iloc[x]['stalk-surface-above-ring'] == 's':
                                            if df.iloc[x]['cap-color'] == 'n' or df.iloc[x]['cap-color'] == 'p' or df.iloc[x]['cap-color'] == 'w':
                                                if df.iloc[x]['population'] == 'a' or df.iloc[x]['population'] == 'c' or df.iloc[x]['population'] == 'n' or df.iloc[x]['population'] == 'y':
                                                    return 'e'
                                                if df.iloc[x]['population'] == 's' or df.iloc[x]['population'] == 'v':
                                                    return 'p'
                                            if df.iloc[x]['cap-color'] == 'g' or df.iloc[x]['cap-color'] == 'y':
                                                if df.iloc[x]['ring-type'] == 'e' or df.iloc[x]['ring-type'] == 'f':
                                                    return 'e'
                                                if df.iloc[x]['ring-type'] == 'p' or df.iloc[x]['ring-type'] == 'l':
                                                    return 'p'
                                            if df.iloc[x]['cap-color'] == 'e':
                                                if df.iloc[x]['gill-color'] == 'b' or df.iloc[x]['gill-color'] == 'k' or df.iloc[x]['gill-color'] == 'p':
                                                    return 'p'
                                                if df.iloc[x]['gill-color'] == 'e' or df.iloc[x]['gill-color'] == 'g' or df.iloc[x]['gill-color'] == 'h' or df.iloc[x]['gill-color'] == 'n' or df.iloc[x]['gill-color'] == 'u' or df.iloc[x]['gill-color'] == 'w':
                                                    return 'e'
                                            if df.iloc[x]['cap-color'] == 'c' or df.iloc[x]['cap-color'] == 'r' or df.iloc[x]['cap-color'] == 'u':
                                                return 'e'
                                            if df.iloc[x]['cap-color'] == 'b':
                                                if df.iloc[x]['population'] == 's' or df.iloc[x]['population'] == 'v' or df.iloc[x]['population'] == 'y':
                                                    if df.iloc[x]['ring-type'] == 'e' or df.iloc[x]['ring-type'] == 'f':
                                                        return 'e'
                                                    if df.iloc[x]['ring-type'] == 'p' or df.iloc[x]['ring-type'] == 'l':
                                                        return 'p'
                                                if df.iloc[x]['population'] == 'a':
                                                    return 'e'
                                                if df.iloc[x]['population'] == 'n':
                                                    return 'e'
                                                if df.iloc[x]['population'] == 'c':
                                                    if df.iloc[x]['ring-type'] == 'e':
                                                        if df.iloc[x]['gill-color'] == 'b' or df.iloc[x]['gill-color'] == 'k' or df.iloc[x]['gill-color'] == 'p':
                                                            return 'p'
                                                        if df.iloc[x]['gill-color'] == 'e' or df.iloc[x]['gill-color'] == 'g' or df.iloc[x]['gill-color'] == 'h' or df.iloc[x]['gill-color'] == 'n' or df.iloc[x]['gill-color'] == 'u' or df.iloc[x]['gill-color'] == 'w':
                                                            return 'e'
                                                    if df.iloc[x]['ring-type'] == 'l':
                                                        return 'p'
                                                    if df.iloc[x]['ring-type'] == 'f':
                                                        return 'e'
                                                    if df.iloc[x]['ring-type'] == 'p':
                                                        if df.iloc[x]['stalk-color-above-ring'] == 'w':
                                                            if df.iloc[x]['cap-shape'] == 'x':
                                                                return 'p'
                                                            if df.iloc[x]['cap-shape'] == 's' or df.iloc[x]['cap-shape'] == 'b' or df.iloc[x]['cap-shape'] == 'k' or df.iloc[x]['cap-shape'] == 'f':
                                                                return 'e'
                                                        if df.iloc[x]['stalk-color-above-ring'] == 'b' or df.iloc[x]['stalk-color-above-ring'] == 'n':
                                                            return 'p'
                                                        if df.iloc[x]['stalk-color-above-ring'] == 'e' or df.iloc[x]['stalk-color-above-ring'] == 'g':
                                                            return 'e'
                                                        if df.iloc[x]['stalk-color-above-ring'] == 'p':
                                                            if df.iloc[x]['gill-color'] == 'n' or df.iloc[x]['gill-color'] == 'u' or df.iloc[x]['gill-color'] == 'w':
                                                                if df.iloc[x]['cap-surface'] == 'y' or df.iloc[x]['cap-surface'] == 's':
                                                                    return 'p'
                                                                if df.iloc[x]['cap-surface'] == 'f':
                                                                    return 'e'
                                                            if df.iloc[x]['gill-color'] == 'h' or df.iloc[x]['gill-color'] == 'k' or df.iloc[x]['gill-color'] == 'p':
                                                                if df.iloc[x]['gill-spacing'] == 'c':
                                                                    return 'p'
                                                                if df.iloc[x]['gill-spacing'] == 'w':
                                                                    return 'e'
                                                            if df.iloc[x]['gill-color'] == 'b':
                                                                return 'p'
                                                            if df.iloc[x]['gill-color'] == 'e':
                                                                return 'e'
                                                            if df.iloc[x]['gill-color'] == 'g':
                                                                if df.iloc[x]['cap-shape'] == 'f':
                                                                    if df.iloc[x]['gill-spacing'] == 'c':
                                                                        return 'p'
                                                                    if df.iloc[x]['gill-spacing'] == 'w':
                                                                        return 'e'
                                                                if df.iloc[x]['cap-shape'] == 'k':
                                                                    if df.iloc[x]['cap-surface'] == 'y' or df.iloc[x]['cap-surface'] == 's':
                                                                        return 'p'
                                                                    if df.iloc[x]['cap-surface'] == 'f':
                                                                        return 'e'
                                                                if df.iloc[x]['cap-shape'] == 'b':
                                                                    if df.iloc[x]['ring-number'] == 't':
                                                                        return 'e'
                                                                    if df.iloc[x]['ring-number'] == 'o':
                                                                        return 'p'
                                                                if df.iloc[x]['cap-shape'] == 's':
                                                                    return 'e'
                                                                if df.iloc[x]['cap-shape'] == 'x':
                                                                    if df.iloc[x]['gill-spacing'] == 'w':
                                                                        if df.iloc[x]['cap-surface'] == 'y' or df.iloc[x]['cap-surface'] == 's':
                                                                            return 'p'
                                                                        if df.iloc[x]['cap-surface'] == 'f':
                                                                            return 'e'
                                                                    if df.iloc[x]['gill-spacing'] == 'c':
                                                                        if df.iloc[x]['cap-surface'] == 's':
                                                                            if df.iloc[x]['ring-number'] == 't' or df.iloc[x]['ring-number'] == 'f':
                                                                                return 'e'
                                                                            if df.iloc[x]['ring-number'] == 'o':
                                                                                return 'p'
                                                                        if df.iloc[x]['cap-surface'] == 'f':
                                                                            return 'e'
                                                                        if df.iloc[x]['cap-surface'] == 'y':
                                                                            if df.iloc[x]['ring-number'] == 't' or df.iloc[x]['ring-number'] == 'f':
                                                                                return 'e'
                                                                            if df.iloc[x]['ring-number'] == 'o':
                                                                                return 'p'                                                           
