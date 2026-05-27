def create_features(df):

    if (
        'kills' in df.columns and
        'walkDistance' in df.columns
    ):

        df[
            'kill_efficiency'
        ] = (

            df['kills']

            /

            (
                df['walkDistance']
                + 1
            )

        )

    if (
        'damageDealt' in df.columns and
        'kills' in df.columns
    ):

        df[
            'damage_per_kill'
        ] = (

            df['damageDealt']

            /

            (
                df['kills']
                + 1
            )

        )

    return df
