import React from "react";

interface Props {
  variant: 'primary' | 'secondary' | 'disabled';
  type?: 'button' | 'submit' | 'reset' | undefined;
  text: string;
  className?: string;
  disabled?: boolean;
  onClick?: () => void;
}

const primaryStyles =
  'inline-block text-sm text-green rounded text-base font-bold cursor-pointer mx-0 my-2 px-4 py-2 border-2 border-solid border-green';

const secondaryStyles =
  'inline-block text-sm text-red rounded text-base font-bold cursor-pointer mx-0 my-2 px-4 py-2 border-2 border-solid border-red';
const disabled =
"inline-block text-sm text-gray rounded text-base font-bold cursor-pointer mx-0 my-2 px-4 py-2 border-2 border-solid border-green opacity-70 cursor-not-allowed"

  const styles = {
    primary: primaryStyles,
    secondary: secondaryStyles,
    disabled: disabled,
  };

const Button: React.FC<Props> = (props: Props) => {
  const classes = `btn ${styles[props.variant]} ${props.className || ''}`;
  const type = props.type || 'button';

  return (
    <button
      className={classes}
      onClick={props.onClick}
      type={type}
      disabled={props.disabled ?? false}
    >
      {props.text}
    </button>
  );
};

export default Button;