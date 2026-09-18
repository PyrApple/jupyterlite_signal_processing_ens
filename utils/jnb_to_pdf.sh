for f in *.ipynb; do

    # execute / save
    # jupyter-nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=300 "$f"

    # export to pdf
    # jupyter-nbconvert --to webpdf "$f"
    jupyter-nbconvert --to pdf "$f"
done