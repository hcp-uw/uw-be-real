def unique_property_constraint(constraint: str, property: str) -> str:
    return f'''
            CREATE CONSTRAINT {constraint}
            IF NOT EXISTS
            FOR (user:User)
            REQUIRE user.{property} IS UNIQUE;
        '''