def anonymize(df):
    """Mask PII columns in health data."""
    return df.withColumn("patient_id", lit("***"))

def validate_schema(df, expected_cols):
    """Check that required columns exist."""
    missing = [c for c in expected_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
