## Aromatic Compunds Viewer

We are creating  web application using the Streamlit framework, designed to display the structures of aromatic compounds based on their SMILES.

The web application provides an interactive and user-friendly interface for visualizing these chemical structures.

## Molecule generation

Generating and Displaying Molecular Structures:
For each SMILES string in the list:
The code generates a subheader with the SMILES string.
It converts the SMILES string into a molecular structure using Chem.MolFromSmiles.
If the molecule is valid, it uses Draw.MolToImage from RDKit to create an image of the molecule.
The image of the molecule is then displayed in the app using st.image.
If the SMILES string is invalid, an error message is displayed.


